from sample_utils import make_env
from mpire import WorkerPool
import numpy as np
import sys
from tqdm import tqdm


def start_episode(worker_id, worker_state, env_name):
    i = 0
    while (env_name, i) in worker_state:
        i += 1
    env_id = (env_name, i)
    env = make_env(env_name, (worker_id << 16) + i)
    worker_state[env_id] = env
    obs = env.reset()
    worker_state[(env_id, 'last_obs')] = obs
    worker_state[(env_id, 'step')] = 0
    return obs, env_id

def step(worker_id, worker_state, action, agent_info, env_id, noise_scale):
    action_noisy = action + np.random.normal(
        scale=noise_scale, size=(action.shape)
    )
    env = worker_state[env_id]
    next_obs, reward, done, info = env.step(action_noisy)
    data = {
        "observation": worker_state[(env_id, 'last_obs')],
        "action": action_noisy,
        "prenoise_action": action,
        "reward": reward,
        "done": done,
        "env_name": env_id[0],
    }
    for (k, v) in info.items():
        assert k not in data
        data[k] = v
    for (k, v) in agent_info.items():
        assert k not in data
        data[k] = v
    worker_state[(env_id, 'step')] += 1
    if done or worker_state[(env_id, 'step')] >= env.max_path_length:
        # Start new episode
        worker_state[(env_id, 'last_obs')] = env.reset()
        worker_state[(env_id, 'step')] = 0
    else:
        worker_state[(env_id, 'last_obs')] = next_obs
    return data, worker_state[(env_id, 'last_obs')]

def gather_res(result_generator):
    """Basically just a matrix transpose"""
    results = None
    for result in result_generator:
        if results is None:
            results = [[] for i in range(len(result))]
        for i, r in enumerate(result):
            results[i].append(r)
    return results

def gather_data(data, episodes, episodes_by_task, env_names, max_path_length):
    for i, d in enumerate(data):
        assert d["env_name"] == env_names[i]
        episodes[i].append(d)
        if d["done"] or len(episodes[i]) >= max_path_length:
            episodes_by_task[env_names[i]].append(episodes[i])
            episodes[i] = []

def dict_seq_to_seq_dict(d, default_len):
    keys = list(d.keys())
    if len(keys) > 0:
        for i in range(len(d[keys[0]])):
            yield { k: d[k][i] for k in keys }
    else:
        for i in range(default_len):
            yield {}

class VecMpireSampler:

    def __init__(self, n_workers: int = 20):
        # n_workers = 100
        assert n_workers % 2 == 0
        n_jobs = n_workers // 2
        main_module = sys.modules["__main__"]
        if not hasattr(main_module, "__spec__"):
            main_module.__spec__ = "MainModule"
        self._pool_a = WorkerPool(n_jobs=n_jobs, use_worker_state=True, pass_worker_id=True, keep_alive=True, start_method='spawn', order_tasks=True)
        self._pool_b = WorkerPool(n_jobs=n_jobs, use_worker_state=True, pass_worker_id=True, keep_alive=True, start_method='spawn', order_tasks=True)

    def collect_episodes(self, policy, env_names, n_episodes, noise_scale, max_path_length=500):
        episodes_by_task = { env_name: [] for env_name in env_names }
        res_a = self._pool_a.imap(start_episode, env_names, chunk_size=1)
        res_b = self._pool_b.imap(start_episode, env_names, chunk_size=1)
        episodes_a = [[] for _ in range(len(env_names))]
        episodes_b = [[] for _ in range(len(env_names))]

        noise_scale_vec = [noise_scale] * len(env_names)

        obs_list_a, env_ids_a = gather_res(res_a)
        actions_a, agent_infos_a = policy.get_actions(obs_list_a, env_names)
        results_a = self._pool_a.map(step, zip(actions_a, dict_seq_to_seq_dict(agent_infos_a, default_len=len(actions_a)), env_ids_a, noise_scale_vec), chunk_size=1)
        obs_list_b, env_ids_b = gather_res(res_b)
        actions_b, agent_infos_b = policy.get_actions(obs_list_b, env_names)
        results_b = self._pool_b.map(step, zip(actions_b, dict_seq_to_seq_dict(agent_infos_b, default_len=len(actions_b)), env_ids_b, noise_scale_vec), chunk_size=1)
        with tqdm(desc="Sampling episodes", total=len(env_names) * n_episodes * max_path_length) as pbar:
            while any(len(episodes) < n_episodes for episodes in episodes_by_task.values()):
                data_a, obs_list_a = gather_res(results_a)
                gather_data(data_a, episodes_a, episodes_by_task, env_names, max_path_length)
                actions_a, agent_infos_a = policy.get_actions(obs_list_a, env_names)
                results_a = self._pool_a.map(step, zip(actions_a, dict_seq_to_seq_dict(agent_infos_a, default_len=len(actions_a)), env_ids_a, noise_scale_vec), chunk_size=1)

                data_b, obs_list_b = gather_res(results_b)
                gather_data(data_b, episodes_b, episodes_by_task, env_names, max_path_length)
                actions_b, agent_infos_b = policy.get_actions(obs_list_b, env_names)
                results_b = self._pool_b.map(step, zip(actions_b, dict_seq_to_seq_dict(agent_infos_b, default_len=len(actions_b)), env_ids_b, noise_scale_vec), chunk_size=1)
                pbar.n = sum([len(ep) for eps in episodes_by_task.values() for ep in eps] + [len(ep) for ep in episodes_a] + [len(ep) for ep in episodes_b])
                pbar.refresh()

        return episodes_by_task
