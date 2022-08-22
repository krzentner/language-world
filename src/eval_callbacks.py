import json
from sample_utils import (
    make_env,
    sample_noisy_policy,
    mean,
    episode_to_success,
    average_reward,
)
import jax_utils
import easy_process
import random
from tqdm import tqdm


N_EVAL_WORKERS = 3


def eval_process(*, env_name, policy, noise_scale: float, parent):
    env = make_env(env_name, random.randrange(1000))
    while True:
        episode = []
        for data in sample_noisy_policy(env, policy, noise_scale):
            data["noise_scale"] = noise_scale
            episode.append(data)
        state_updates = parent.sendrecv(episode)
        if state_updates:
            policy.state = policy.state.replace(params=state_updates[-1])
            parent.sendrecv("policy updated")


class SingleProcEvalCallbacks(jax_utils.FitCallbacks):
    def __init__(
        self,
        seed,
        env_names,
        agent,
        noise_scale=0.10,
        base_infos=None,
        results_proc=None,
        output_filename=None,
    ):
        self.envs = {env_name: make_env(env_name, seed) for env_name in env_names}
        self.noise_scale = noise_scale
        self.agent = agent
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

    def minibatch_start(self, state):
        return state, {}

    def epoch_start(self, state):
        self.current_step += 1
        if self.current_step % self.step_period == 1:
            return self.training_complete(state)
        else:
            return state, {}

    def _run_evals(self, state):
        infos = self.base_infos.copy()
        for (env_name, env) in self.envs.items():
            policy = self.agent.as_policy(env_name, state)
            successes = []
            rewards = []
            with tqdm(total=self.n_episodes) as pbar:
                while len(successes) < self.n_episodes:
                    episode = list(sample_noisy_policy(env, policy, self.noise_scale))
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

    def training_complete(self, state):
        infos = self._run_evals(state)
        if self.results_proc is not None:
            print("Sending back results")
            self.results_proc.sendrecv(infos)
        return state, infos


class EvalCallbacks(jax_utils.FitCallbacks):
    def __init__(
        self,
        seed,
        env_names,
        agent,
        noise_scale=0.10,
        base_infos=None,
        results_proc=None,
        output_filename=None,
    ):
        self.envs = {env_name: make_env(env_name, seed) for env_name in env_names}
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

    def epoch_start(self, state):
        self.current_step += 1
        if self.current_step % self.step_period == 1:
            return self.training_complete(state)
        else:
            return state, {}

    def _run_evals(self, state):
        infos = self.base_infos.copy()
        for (env_name, env) in self.envs.items():
            policy = self.agent.as_policy(env_name, state)
            if env_name in self.workers:
                workers = self.workers[env_name]
                for worker in workers:
                    worker.send(state.params, block=True)
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

            successes = []
            rewards = []
            with tqdm(total=self.n_episodes) as pbar:
                while len(successes) < self.n_episodes:
                    for worker in workers:
                        episode = worker.recv(block=False)
                        if episode is not None and episode != "policy updated":
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

    def training_complete(self, state):
        infos = self._run_evals(state)
        if self.results_proc is not None:
            print("Sending back results")
            self.results_proc.sendrecv(infos)
        if self.process_scope:
            self.process_scope.close()
        return state, infos


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
