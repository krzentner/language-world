import random
import easy_process
import sample_utils
import itertools
from collections import deque
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
from gaussian_noise_process import GaussianNoiseProcess
from run_utils import float_list, str_list
from collections import defaultdict
from mpire import WorkerPool


def single_env_dataset(
    *,
    env_name: str,
    n_timesteps=500,
    seed=sample_utils.DEFAULT_SEED,
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
            noise_proc = GaussianNoiseProcess(
                dimensions=env.action_space.shape[0], noise_scale=noise_scale
            )
            episode = []
            for data in sample_policy_with_noise_process(env, policy, noise_proc):
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


def sample_process(*, env_name: str, noise_scales: [float], seed: int, n_timesteps: int, parent):
    env = make_env(env_name, seed)
    policy = SawyerUniversalV2Policy(env_name=env_name)
    timesteps_so_far = 0

    while True:
        random.shuffle(noise_scales)
        for noise_scale in noise_scales:
            noise_proc = GaussianNoiseProcess(
                dimensions=env.action_space.shape[0], noise_scale=noise_scale
            )
            episode = []
            for data in sample_policy_with_noise_process(env, policy, noise_proc):
                data["env_name"] = env_name
                data["noise_scale"] = noise_scale
                episode.append(data)
                timesteps_so_far += 1
            parent.sendrecv(episode)
        if timesteps_so_far >= n_timesteps:
            break


def mpire_sample_proc(env_name: str, noise_scale: [float], seed: int, n_timesteps: int, parent):
    env = make_env(env_name, seed)
    policy = SawyerUniversalV2Policy(env_name=env_name)
    timesteps_so_far = 0

    while True:
        random.shuffle(noise_scales)
        for noise_scale in noise_scales:
            noise_proc = GaussianNoiseProcess(
                dimensions=env.action_space.shape[0], noise_scale=noise_scale
            )
            episode = []
            for data in sample_policy_with_noise_process(env, policy, noise_proc):
                data["env_name"] = env_name
                data["noise_scale"] = noise_scale
                episode.append(data)
                timesteps_so_far += 1
            parent.sendrecv(episode)
        if timesteps_so_far >= n_timesteps:
            break


def sample_process_buffered(
    *,
    env_name: str,
    noise_scales: [float],
    seed: int,
    episodes_to_buffer: int = 100,
    parent,
):
    env = make_env(env_name, seed)
    policy = SawyerUniversalV2Policy(env_name=env_name)

    episodes = deque(maxlen=episodes_to_buffer)
    while True:
        random.shuffle(noise_scales)
        for noise_scale in noise_scales:
            noise_proc = GaussianNoiseProcess(
                dimensions=env.action_space.shape[0], noise_scale=noise_scale
            )
            episode = []
            for data in sample_policy_with_noise_process(env, policy, noise_proc):
                data["env_name"] = env_name
                data["noise_scale"] = noise_scale
                episode.append(data)
            episodes.append(episode)
            if len(episodes) >= episodes_to_buffer:
                parent.sendrecv(episode.popleft())
            else:
                if parent.send(episodes[0], block=False, timeout=0.5):
                    episodes.popleft()


def grouped_env_dataset_buffered(
    *,
    envs: str_list,
    n_timesteps=1000,
    seed=sample_utils.DEFAULT_SEED,
    shuffle_timesteps=True,
    noise_scales: float_list = [0.1, 0.2, 0.3, 0.4],
) -> [[dict]]:
    """Produce a set of datapoints that each contain one timestep from each env."""
    scope = easy_process.Scope()
    try:
        workers = [
            easy_process.Subprocess(
                sample_process_buffered,
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


def grouped_env_dataset(
    *,
    envs: str_list,
    n_timesteps=1000,
    seed=sample_utils.DEFAULT_SEED,
    shuffle_timesteps=True,
    noise_scales: float_list = [0.1, 0.2, 0.3, 0.4],
) -> [[dict]]:
    """Produce a set of datapoints that each contain one timestep from each env."""
    scope = easy_process.Scope()
    try:
        workers = [
            easy_process.Subprocess(
                sample_process,
                kwargs=dict(env_name=env_name, seed=seed, noise_scales=noise_scales, n_timesteps=n_timesteps),
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
                    # print(f"Collecting episode for {env_name}")
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


def grouped_env_dataset_mpire(
    *,
    envs: str_list,
    n_timesteps=1000,
    seed=sample_utils.DEFAULT_SEED,
    shuffle_timesteps=True,
    noise_scales: float_list = [0.1, 0.2, 0.3, 0.4],
) -> [[dict]]:
    """Produce a set of datapoints that each contain one timestep from each env."""
    assert n_timesteps % len(envs) == 0
    assert n_timesteps % 500 == 0
    timesteps_per_env = n_timesteps // len(envs)
    assert timesteps_per_env % 500 == 0
    episodes_per_env = timesteps_per_env // 500
    episode_keys = []
    while len(episode_keys) < n_timesteps // 500:
        for noise_scale in itertools.cycle(noise_scales):
            for env_name in envs:
                seed += 1
                episode_keys.append((env_name, noise_scale, seed))
            if len(episode_keys) >= n_timesteps // 500:
                break

    def mpire_task(worker_state, env_name, noise_scale, seed):
        if env_name in worker_state:
            env = worker_state[env_name]
        else:
            env = make_env(env_name, seed=seed)
            worker_state[env_name] = env
        policy = SawyerUniversalV2Policy(env_name=env_name)
        noise_proc = GaussianNoiseProcess(
            dimensions=env.action_space.shape[0], noise_scale=noise_scale
        )
        episode = []
        for data in sample_policy_with_noise_process(env, policy, noise_proc):
            data["env_name"] = env_name
            data["noise_scale"] = noise_scale
            episode.append(data)
        return episode

    with WorkerPool(n_jobs=20, use_worker_state=True, keep_alive=True) as pool:
        episodes = pool.map(mpire_task, episode_keys, progress_bar=True, progress_bar_options=dict(desc="Gathering dataset"))
    timesteps_by_task = { env_name: [] for env_name in envs }
    for episode in episodes:
        timesteps_by_task[episode[0]["env_name"]].extend(episode)
    episodes_by_task = { env_name: [] for env_name in envs }
    for episode in episodes:
        episodes_by_task[episode[0]["env_name"]].append(episode)
    calc_success_rates(episodes_by_task)
    if shuffle_timesteps:
        for timesteps in timesteps_by_task:
            random.shuffle(episode)
    for env_name in envs:
        assert len(timesteps_by_task[env_name]) == timesteps_per_env, env_name
    datapoints = [[timesteps_by_task[env_name][i] for env_name in envs]
                  for i in range(timesteps_per_env)]
    return datapoints


def calc_success_rates(episodes_by_task):
    success_rates = {}
    for env_name, episodes in episodes_by_task.items():
        success_rates[env_name] = mean([episode_to_success(ep) for ep in episodes])
    for (env_name, success_rate) in success_rates.items():
        print(f"Data success rate for {env_name}:", success_rate)
    return success_rates



if __name__ == "__main__":
    single_env_dataset(env_name="pick-place", noise_scales=[0.0])
    grouped_env_dataset(envs=["pick-place", "push"], noise_scales=[0.0])
