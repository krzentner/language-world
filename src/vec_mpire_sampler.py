from sample_utils import make_env
from mpire import WorkerPool

def start_episode(worker_id, worker_state, env_name):
    i = 0
    while (env_name, i) in worker_state:
        i += 1
    env_id = (env_name, i)
    env = make_env(env_name, (worker_id << 16) + i)
    worker_state[env_id] = env
    obs = env.reset()
    worker_state[(env_id, 'last_obs')] = obs
    return obs, env_id

def step(worker_id, worker_state, action, agent_info, env_id):
    next_obs, reward, done, info = worker_state[env_id].step(action)
    data = {
        "observation": worker_state[(env_id, 'last_obs')],
        "action": action,
        "reward": reward,
        "done": done,
    }
    for (k, v) in info.items():
        assert k not in data
        data[k] = v
    for (k, v) in agent_info.items():
        assert k not in data
        data[k] = v[i]
    if done:
        # Start new episode
        worker_state[(env_id, 'last_obs')] = env.reset()
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

def gather_data(data, episodes, episodes_by_task, env_names):
    for i, d in enumerate(data):
        assert d["env_name"] == env_names[i]
        episodes[i].append(d)
        if d["done"]:
            episodes_by_task[env_names[i]].append(episodes[i])
            episodes[i] = []

class VecMpireSampler:

    def __init__(self, n_workers: int = 20):
        assert n_workers % 2 == 0
        n_jobs = n_workers // 2
        self._pool_a = WorkerPool(n_jobs=n_jobs, use_worker_state=True, pass_worker_id=True, keep_alive=True)
        self._pool_a.set_order_tasks()
        self._pool_b = WorkerPool(n_jobs=n_jobs, use_worker_state=True, pass_worker_id=True, keep_alive=True)
        self._pool_b.set_order_tasks()

    def collect_episodes(self, policy, env_names, n_episodes):
        episodes_by_task = { env_name: [] for env_name in env_names }
        res_a = self._pool_a.imap(start_episode, env_names)
        res_b = self._pool_b.imap(start_episode, env_names)
        episodes_a = [[] for _ in range(len(env_names))]
        episodes_b = [[] for _ in range(len(env_names))]

        obs_list_a, env_ids_a = gather_res(res_a)
        actions_a, agent_infos_a = policy.get_actions(obs_list_a)
        results_a = self._pool_a.map(step, zip(actions_a, agent_infos_a, env_ids_a))
        obs_list_b, env_ids_a = gather_res(res_b)
        actions_b, agent_infos_b = policy.get_actions(obs_list_b)
        results_b = self._pool_b.map(step, zip(actions_b, agent_infos_b, env_ids_b))
        while any(len(episodes) < n_episodes for episodes in episodes_by_task.values()):
            data_a, obs_list_a = gather_res(results_a)
            actions_a, agent_infos_a = policy.get_actions(obs_list_a)

            gather_data(data_a, episodes_a, episodes_by_task, env_names)

            data_b, obs_list_b = gather_res(results_b)
            actions_b, agent_infos_b = policy.get_actions(obs_list_b)

            gather_data(data_b, episodes_b, episodes_by_task, env_names)
        return episodes_by_task
