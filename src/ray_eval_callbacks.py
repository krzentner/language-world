import json
from sample_utils import (
    make_env,
    sample_noisy_policy,
    mean,
    episode_to_success,
    average_reward,
    vec_collect_noisy_episodes,
    vec_sample_noisy_policy,
    calc_statistics,
)
import pytorch_utils
import easy_process
import random
from tqdm import tqdm
import ray


VEC_ENVS = 5


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
