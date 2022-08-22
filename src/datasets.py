import random
import jax_utils
import easy_process
from sample_utils import (
    make_env,
    sample_policy_with_noise_process,
    mean,
    episode_to_success,
    average_reward,
)
from metaworld_universal_policy import SawyerUniversalV2Policy
from tqdm import tqdm
from ou_process import OUProcess
from run_utils import float_list, str_list
from collections import defaultdict


def single_env_dataset(
    *,
    env_name: str,
    n_timesteps=500,
    seed=jax_utils.DEFAULT_SEED,
    shuffle_timesteps=True,
    noise_scales: float_list = [0.1],
) -> [dict]:
    """Produce a set of datapoints that each contain one timestep from each env."""
    env = make_env(env_name, seed)
    policy = SawyerUniversalV2Policy(env_name=env_name)
    datapoints = []
    successes = []

    assert len(noise_scales) * env.max_episode_length <= n_timesteps

    random.shuffle(noise_scales)
    with tqdm(total=n_timesteps) as pbar:
        for noise_scale in noise_scales:
            ou_proc = OUProcess(dimensions=env.action_space.shape[0], sigma=noise_scale)
            episode = []
            for data in sample_policy_with_noise_process(env, policy, ou_proc):
                data["env_name"] = env_name
                data["noise_scale"] = noise_scale
                episode.append(data)
                pbar.update(1)
            successes.append(episode_to_success(episode))
            datapoints.extend(episode)
    if shuffle_timesteps:
        random.shuffle(datapoints)
    print(f"Data success rate for {env_name}:", mean(successes))
    return datapoints


def sample_process(*, env_name: str, noise_scales: [float], seed: int, parent):
    env = make_env(env_name, seed)
    policy = SawyerUniversalV2Policy(env_name=env_name)

    while True:
        random.shuffle(noise_scales)
        for noise_scale in noise_scales:
            ou_proc = OUProcess(dimensions=env.action_space.shape[0], sigma=noise_scale)
            episode = []
            for data in sample_policy_with_noise_process(env, policy, ou_proc):
                data["env_name"] = env_name
                data["noise_scale"] = noise_scale
                episode.append(data)
            parent.sendrecv(episode)


def grouped_env_dataset(
    *,
    envs: str_list,
    n_timesteps=1000,
    seed=jax_utils.DEFAULT_SEED,
    shuffle_timesteps=True,
    noise_scales: float_list = [0.1, 0.2, 0.3, 0.4],
) -> [[dict]]:
    """Produce a set of datapoints that each contain one timestep from each env."""
    scope = easy_process.Scope()
    try:
        workers = [
            easy_process.Subprocess(
                sample_process,
                kwargs=dict(env_name=env_name, seed=seed, noise_scales=noise_scales),
                scope=scope,
            )
            for env_name in envs
        ]
        datapoints = []
        successes = defaultdict(list)
        with tqdm(total=n_timesteps) as pbar:
            while len(datapoints) < n_timesteps:
                episode_block = []
                for (env_name, worker) in zip(envs, workers):
                    episode = worker.recv(block=True)
                    successes[env_name].append(episode_to_success(episode))
                    if shuffle_timesteps:
                        random.shuffle(episode)
                    episode_block.append(episode)
                new_datapoints = min(len(episode) for episode in episode_block)
                for i in range(new_datapoints):
                    datapoints.append([episode[i] for episode in episode_block])
                pbar.update(new_datapoints)
    finally:
        scope.close()
    for (env_name, success_rate) in successes.items():
        print(f"Data success rate for {env_name}:", mean(success_rate))
    return datapoints
