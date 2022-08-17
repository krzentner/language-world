from doexp import cmd, In, Out
from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES

cmd('python', 'src/find_most_likely_plans.py', Out('controller_map.pkl'))
cmd('python', 'src/plot_tasks_at_success_rate.py', '--out-file', Out('cond_agent_v0_success_rates.html'))

for env_name in MT50_ENV_NAMES:
  cmd('python', 'src/render_policy.py',
      '--env-name', env_name,
      '--out-file', Out(f'render_policy/universal_policy/{env_name}_universal-policy.mp4'),
      extra_outputs=[Out(f'render_policy/universal_policy/{env_name}_universal-policy.gif')])

cmd('python', 'src/diff_agent.py',
    '--out-success', Out('diff-agent_success.json'),
    '--out-avg-reward', Out('diff-agent_avg-reward.json'),
    '--render-output-dir', Out('render_policy/diff_agent/'))

cmd('python', 'src/evaluator_agent.py', 'zeroshot',
    '--language-space-mixing=no',
    '--plan-file', 'mt50_plans_v0.py',
    '--out-file', Out('cond_agent_v0_results_no_mix.json'))
