from doexp import cmd, In, Out, GLOBAL_CONTEXT
from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES
import psutil
GLOBAL_CONTEXT.vm_percent_cap = 25.

# cmd('python', 'src/find_most_likely_plans.py', Out('controller_map.pkl'))
# cmd('python', 'src/plot_tasks_at_success_rate.py', '--out-file', Out('cond_agent_v0_success_rates.html'))
cmd('python', 'src/plot_tasks_at_success_rate.py', '--out-file', Out('success_rates.html'))
cmd('python', 'src/plot_tasks_at_success_rate.py', '--ignore-mt10', '--out-file', Out('success_rates_no_mt10.html'))
cmd('python', 'src/write_v0_results.py',
    '--oneshot-success-out', Out('cond_agent_v0_success_rate_one_shot.json'),
    '--zeroshot-success-out', Out('cond_agent_v0_success_rate_zero_shot.json'),
    )

# cmd('python', 'src/plot_tasks_at_success_rate.py',
    # '--title', "Transfer Success Rate",
    # '--out-file', Out('cond_agent_success_rates.html'),
    # '--in-file', In('cond_agent_v0_success_rate_one_shot.json'),
    # '--label', "Cond Agent V0 One Shot",
    # '--in-file', In('cond_agent_v0_success_rate_zero_shot.json'),
    # '--label', "Cond Agent V0 Zero Shot",
    # '--in-file', In('diff-agent_success.json'),
    # '--label', "Diff Agent",
    # )

for env_name in MT50_ENV_NAMES:
  cmd('python', 'src/render_policy.py',
      '--env-name', env_name,
      '--out-file', Out(f'render_policy/universal_policy/{env_name}_universal-policy.mp4'),
      extra_outputs=[Out(f'render_policy/universal_policy/{env_name}_universal-policy.gif')])

cmd('python', 'src/diff_agent.py',
    '--out-success', Out('diff-agent_success.json'),
    '--out-avg-reward', Out('diff-agent_avg-reward.json'),
    '--render-output-dir', Out('render_policy/diff_agent/'))

cmd('python', 'src/diff_agent.py',
    '--plan-file', 'mt50_plans_projected.py',
    '--out-success', Out('diff-agent-proj_success.json'),
    '--out-avg-reward', Out('diff-agent-proj_avg-reward.json'),
    '--render-output-dir', Out('render_policy/diff_agent_proj/'))

cmd('python', 'src/evaluator_agent.py', 'zeroshot',
    '--language-space-mixing=no',
    '--plan-file', 'mt50_plans_v0.py',
    '--out-file', Out('cond_agent_v0_results_no_mix.json'),
    warmup_time=30)

if psutil.virtual_memory().percent <= 15:
  cmd('python', 'src/evaluator_agent.py', 'zeroshot',
      '--plan-file', 'mt50_plans_v1.py',
      '--out-file', Out('cond_agent_v1_zeroshot.ndjson'),
      warmup_time=600)

# for env_name in MT50_ENV_NAMES:
  # cmd('python', 'src/evaluator_agent.py', 'fewshot',
      # '--language-space-mixing=no',
      # '--plan-file', 'mt50_plans_v1.py',
      # '--target-env', env_name,
      # '--out-file', Out(f'cond_agent_v1_fewshot_no_mix-{env_name}.ndjson'),
      # warmup_time=210)

# for env_name in MT50_ENV_NAMES:
  # cmd('python', 'src/evaluator_agent.py', 'fewshot',
      # '--plan-file', 'mt50_plans_v1.py',
      # '--target-env', env_name,
      # '--out-file', Out(f'cond_agent_v1_fewshot-{env_name}.ndjson'),
      # warmup_time=180)

# for env_name in MT50_ENV_NAMES:
  # cmd('python', 'src/evaluator_agent.py', 'fewshot',
      # '--plan-file', 'mt50_plans_v1.py',
      # '--target-env', env_name,
      # '--use-noise', 'no',
      # '--out-file', Out(f'cond_agent_v1_fewshot-{env_name}-no-noise.ndjson'),
      # warmup_time=180)

# for env_name in MT50_ENV_NAMES:
  # cmd('python', 'src/mlp_agent.py', 'fewshot',
      # '--target-env', env_name,
      # '--out-file', Out(f'mlp_agent_v1_fewshot-{env_name}-500-epochs.ndjson'),
      # warmup_time=60)

for env_name in MT50_ENV_NAMES:
  cmd('python', 'src/mlp_agent.py', 'fewshot',
      '--target-env', env_name,
      '--use-noise', 'no',
      '--out-file', Out(f'mlp_agent_v1_fewshot-{env_name}-no-noise.ndjson'),
      warmup_time=60)
