import json
from sample_utils import (
    make_env,
    sample_noisy_policy,
    mean,
    episode_to_success,
    average_reward,
    vec_collect_noisy_episodes,
    vec_sample_noisy_policy,
)
import pytorch_utils
import easy_process
import random
from tqdm import tqdm
import ray


N_EVAL_WORKERS = 1
VEC_ENVS = 5


def eval_process(*, env_name, policy, noise_scale: float, parent):
    envs = [make_env(env_name, random.randrange(1000)) for i in range(VEC_ENVS)]
    while True:
        episodes = vec_sample_noisy_policy(envs, policy, noise_scale)
        state_updates = parent.sendrecv(episodes)
        if state_updates:
            policy.agent.load_state_dict(state_updates[-1])
            parent.sendrecv("policy updated")


@ray.remote
class RayEvalWorker(pytorch_utils.FitCallbacks):
    def __init__(self, env_name, policy, noise_scale: float, seed):
        self.envs = [make_env(env_name, seed) for i in range(VEC_ENVS)]
        self.policy = policy
        self.noise_scale = noise_scale

    def get_batch(self, *, state_dict, n_episodes):
        self.policy.agent.load_state_dict(state_dict)
        return vec_collect_noisy_episodes(
            self.envs, self.policy, self.noise_scale, n_episodes
        )


class RayEvalCallbacks(pytorch_utils.FitCallbacks):
    def __init__(
        self,
        seed,
        env_names,
        agent,
        noise_scale=0.10,
        base_infos=None,
        results_proc=None,
        output_filename=None,
        step_period=20,
        n_episodes=50,
    ):
        self.n_episodes = n_episodes
        self.step_period = step_period
        print("Spinning up ray eval workers")
        self.workers = {
            env_name: RayEvalWorker.remote(
                env_name, agent.as_policy(env_name), noise_scale, seed + i
            )
            for (i, env_name) in tqdm(enumerate(env_names))
        }
        print("Done spinning up ray eval workers")
        self.noise_scale = noise_scale
        self.current_step = 0
        if base_infos is None:
            base_infos = {}
        self.base_infos = base_infos
        self.results_proc = results_proc
        self.output_filename = output_filename
        if output_filename:
            with open(output_filename, "w") as f:
                # Truncate the output file
                pass

    def minibatch_start(self, agent):
        return {}

    def epoch_start(self, agent):
        self.current_step += 1
        if self.current_step % self.step_period == 1:
            return self.training_complete(agent)
        else:
            return {}

    def _run_evals(self, agent):
        print("Evaluating...")
        infos = self.base_infos.copy()
        results = {}
        for (env_name, worker) in self.workers.items():
            results[env_name] = worker.get_batch.remote(
                state_dict=agent.state_dict(), n_episodes=self.n_episodes
            )
        for (env_name, result) in results.items():
            successes = []
            rewards = []
            episodes = ray.get(result)
            for episode in episodes:
                successes.append(episode_to_success(episode))
                rewards.append(average_reward(episode))
            print(f"Success rate for {env_name}:", mean(successes))
            infos[f"{env_name}/SuccessRate"] = mean(successes)
            infos[f"{env_name}/RewardMean"] = mean(rewards)
        if self.output_filename:
            with open(self.output_filename, "a") as f:
                json.dump(infos, f)
                f.write("\n")
        return infos

    def training_complete(self, agent):
        infos = self._run_evals(agent)
        if self.results_proc is not None:
            print("Sending back results")
            self.results_proc.sendrecv(infos)
        return infos


class SingleProcEvalCallbacks(pytorch_utils.FitCallbacks):
    def __init__(
        self,
        seed,
        env_names,
        agent,
        noise_scale=0.10,
        base_infos=None,
        results_proc=None,
        output_filename=None,
        step_period=20,
        n_episodes=50,
    ):
        self.n_episodes = n_episodes
        self.step_period = step_period
        print("Creating eval environments")
        self.envs = {
            env_name: [make_env(env_name, seed + i) for i in range(20)]
            for env_name in tqdm(env_names)
        }
        print("Done creating eval environments")
        self.noise_scale = noise_scale
        self.agent = agent
        self.current_step = 0
        if base_infos is None:
            base_infos = {}
        self.base_infos = base_infos
        self.results_proc = results_proc
        self.output_filename = output_filename
        if output_filename:
            with open(output_filename, "w") as f:
                # Truncate the output file
                pass

    def minibatch_start(self, agent):
        return {}

    def epoch_start(self, agent):
        self.current_step += 1
        if self.current_step % self.step_period == 1:
            return self.training_complete(agent)
        else:
            return {}

    def _run_evals(self, agent):
        print("Evaluating...")
        infos = self.base_infos.copy()
        for (env_name, envs) in self.envs.items():
            self.agent.load_state_dict(agent.state_dict())
            policy = self.agent.as_policy(env_name)
            successes = []
            rewards = []
            episodes = vec_collect_noisy_episodes(
                envs, policy, self.noise_scale, self.n_episodes
            )
            for episode in episodes:
                successes.append(episode_to_success(episode))
                rewards.append(average_reward(episode))
            print(f"Success rate for {env_name}:", mean(successes))
            infos[f"{env_name}/SuccessRate"] = mean(successes)
            infos[f"{env_name}/RewardMean"] = mean(rewards)
        if self.output_filename:
            with open(self.output_filename, "a") as f:
                json.dump(infos, f)
                f.write("\n")
        return infos

    def training_complete(self, agent):
        infos = self._run_evals(agent)
        if self.results_proc is not None:
            print("Sending back results")
            self.results_proc.sendrecv(infos)
        return infos


class EvalCallbacks(pytorch_utils.FitCallbacks):
    def __init__(
        self,
        seed,
        env_names,
        agent,
        noise_scale=0.10,
        base_infos=None,
        results_proc=None,
        output_filename=None,
        step_period=20,
        n_episodes=50,
    ):
        self.n_episodes = n_episodes
        self.step_period = step_period
        self.env_names = env_names
        self.noise_scale = noise_scale
        self.agent = agent
        self.process_scope = easy_process.Scope()
        self.workers = {}
        self.n_episodes = 50
        self.step_period = 20
        self.current_step = 0
        if base_infos is None:
            base_infos = {}
        self.base_infos = base_infos
        self.results_proc = results_proc
        self.output_filename = output_filename
        if output_filename:
            with open(output_filename, "w") as f:
                # Truncate the output file
                pass

    def epoch_start(self, agent):
        self.current_step += 1
        if self.current_step % self.step_period == 1:
            return self.training_complete()
        else:
            return {}

    def _run_evals(self, agent):
        infos = self.base_infos.copy()
        for env_name in self.env_names:
            policy = self.agent.as_policy(env_name)
            if env_name in self.workers:
                workers = self.workers[env_name]
                for worker in workers:
                    worker.send(agent.state_dict(), block=True)
                for worker in workers:
                    msg = None
                    while msg != "policy updated":
                        msg = worker.recv(block=True)
            else:
                workers = [
                    easy_process.Subprocess(
                        eval_process,
                        kwargs=dict(
                            env_name=env_name,
                            policy=policy,
                            noise_scale=self.noise_scale,
                        ),
                        scope=self.process_scope,
                    )
                    for _ in range(N_EVAL_WORKERS)
                ]
                self.workers[env_name] = workers

        for env_name in self.env_names:
            successes = []
            rewards = []
            with tqdm(total=self.n_episodes) as pbar:
                while len(successes) < self.n_episodes:
                    for worker in self.workers[env_name]:
                        episodes = worker.recv(block=False)
                        if episodes is not None and episodes != "policy updated":
                            for episode in episodes:
                                successes.append(episode_to_success(episode))
                                rewards.append(average_reward(episode))
                                pbar.update(1)
            print(f"Success rate for {env_name}:", mean(successes))
            infos[f"{env_name}/SuccessRate"] = mean(successes)
            infos[f"{env_name}/RewardMean"] = mean(rewards)
        if self.output_filename:
            with open(self.output_filename, "a") as f:
                json.dump(infos, f)
                f.write("\n")
        return infos

    def training_complete(self, agent):
        infos = self._run_evals()
        if self.results_proc is not None:
            print("Sending back results")
            self.results_proc.sendrecv(infos)
        if self.process_scope:
            self.process_scope.close()
        return infos


def evaluate_policy(env_name, n_episodes, env, policy, noise_scale):
    successes = []
    if n_episodes <= 10:
        for i in tqdm(range(n_episodes)):
            successes.append(
                episode_to_success(sample_noisy_policy(env, policy, noise_scale))
            )
    else:
        scope = easy_process.Scope()
        try:
            workers = []
            for _ in range(N_EVAL_WORKERS):
                workers.append(
                    easy_process.Subprocess(
                        eval_process,
                        kwargs=dict(env=env, policy=policy, noise_scale=noise_scale),
                        scope=scope,
                    )
                )
            with tqdm(total=n_episodes) as pbar:
                while len(successes) < n_episodes:
                    for worker in workers:
                        episode = worker.recv(block=False)
                        if episode is not None and episode != "policy updated":
                            successes.append(episode_to_success(episode))
                            pbar.update(1)
        finally:
            scope.close()
    print("Success rate for", env_name, ":", mean(successes))
    return mean(successes)