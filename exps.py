from doexp import cmd, FileArg, In, Out, GLOBAL_CONTEXT
import psutil

GLOBAL_CONTEXT.max_concurrent_jobs = 20
GLOBAL_CONTEXT.vm_percent_cap = 90.0

MT50_ENV_NAMES = [
    "assembly",
    "basketball",
    "bin-picking",
    "box-close",
    "button-press-topdown",
    "button-press-topdown-wall",
    "button-press",
    "button-press-wall",
    "coffee-button",
    "coffee-pull",
    "coffee-push",
    "dial-turn",
    "disassemble",
    "door-close",
    "door-lock",
    "door-open",
    "door-unlock",
    "hand-insert",
    "drawer-close",
    "drawer-open",
    "faucet-open",
    "faucet-close",
    "hammer",
    "handle-press-side",
    "handle-press",
    "handle-pull-side",
    "handle-pull",
    "lever-pull",
    "peg-insert-side",
    "pick-place-wall",
    "pick-out-of-hole",
    "reach",
    "push-back",
    "push",
    "pick-place",
    "plate-slide",
    "plate-slide-side",
    "plate-slide-back",
    "plate-slide-back-side",
    "peg-unplug-side",
    "soccer",
    "stick-push",
    "stick-pull",
    "push-wall",
    "reach-wall",
    "shelf-place",
    "sweep-into",
    "sweep",
    "window-open",
    "window-close",
]

MT10_ENV_NAMES = [
    "reach",
    "push",
    "pick-place",
    "door-open",
    "drawer-open",
    "drawer-close",
    "button-press-topdown",
    "peg-insert-side",
    "window-open",
    "window-close",
]

MT40_ENV_NAMES = []
for env_name in MT50_ENV_NAMES:
    if env_name not in MT10_ENV_NAMES:
        MT40_ENV_NAMES.append(env_name)

GPT3_ENGINES = [
    # "text-babbage-001",
    # "text-curie-001",
    "text-davinci-003",
]

GPT_CHAT_MODELS = [
    # "gpt-4",
    "gpt-3.5-turbo"
]

PLAN_ENCODINGS = [
    "basic_py",
    "chain_py",
    "goal_py",
    "basic_py_md",
    "chain_py_md",
    "goal_py_md",
    "basic_md",
    "chain_md",
    "goal_md",
]

LLM_ATTEMPTS = 5


def plan_ext(plan_enc):
    if plan_enc.endswith("_py_md"):
        return ".py.md"
    elif plan_enc.endswith("_md"):
        return ".md"
    elif plan_enc.endswith("_py"):
        return ".py"
    else:
        return ".plan"


cmd(
    "python",
    "src/plan_encoding.py",
    "generate-all-plans",
    In("."),
    extra_outputs=[
        Out(f"{plan_enc}/{task}{plan_ext(plan_enc)}")
        for plan_enc in PLAN_ENCODINGS
        for task in MT50_ENV_NAMES
    ],
    ram_gb=0.3,
)

for plan_enc in PLAN_ENCODINGS:
    ext = plan_ext(plan_enc)
    for task in MT50_ENV_NAMES:
        for gpt3_engine in GPT3_ENGINES:
            cmd(
                "python",
                "src/gpt_completion.py",
                In(f"{plan_enc}/{task}{ext}"),
                FileArg(f"{gpt3_engine}/{plan_enc}/{task}-{{i}}{ext}"),
                f"--n-outputs={LLM_ATTEMPTS}",
                extra_outputs=[
                    Out(f"{gpt3_engine}/{plan_enc}/{task}-{i}{ext}")
                    for i in range(LLM_ATTEMPTS)
                ],
                warmup_time=1,
                ram_gb=0.3,
                priority=0,
            )
        for gpt_model in GPT_CHAT_MODELS:
            cmd(
                "python",
                "src/gpt_chat.py",
                In(f"{plan_enc}/{task}{ext}"),
                FileArg(f"{gpt_model}/{plan_enc}/{task}-{{i}}{ext}"),
                f"--n-outputs={LLM_ATTEMPTS}",
                extra_outputs=[
                    Out(f"{gpt_model}/{plan_enc}/{task}-{i}{ext}")
                    for i in range(LLM_ATTEMPTS)
                ],
                warmup_time=1,
                ram_gb=0.3,
                priority=1,
            )
        for model in GPT3_ENGINES + GPT_CHAT_MODELS:
            for i in range(LLM_ATTEMPTS):
                cmd(
                    "python",
                    "src/scripted_cond_agent.py",
                    f"--task={task}",
                    In("{model}/{plan_enc}/{task}-{i}{ext}"),
                    Out("{model}/{plan_enc}/{task}-{i}-perf.json"),
                )

# print(GLOBAL_CONTEXT.commands)
# cmd('python', 'src/find_most_likely_plans.py', Out('controller_map.pkl'))
# cmd('python', 'src/plot_tasks_at_success_rate.py', '--out-file', Out('cond_agent_v0_success_rates.html'))
# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--out-file",
# Out("success_rates.html"),
# )

# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--ignore-mt10",
# "--out-file",
# Out("success_rates_no_mt10.html"),
# )

# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--ignore-mt10",
# "--result-set",
# "best",
# "--out-file",
# Out("success_rates_best.html"),
# )

# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--ignore-mt10",
# "--result-set",
# "zeroshot",
# "--out-file",
# Out("success_rates_zeroshot.html"),
# )

# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--ignore-mt10",
# "--result-set",
# "zeroshot-no-noise",
# "--out-file",
# Out("success_rates_zeroshot-no-noise.html"),
# )

# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--ignore-mt10",
# "--result-set",
# "language-world",
# "--out-file",
# Out("success_rates_language-world.html"),
# )

# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--ignore-mt10",
# "--result-set",
# "noise-difference",
# "--out-file",
# Out("success_rates_abr.html"),
# )

# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--ignore-mt10",
# "--result-set",
# "no-mix",
# "--out-file",
# Out("success_rates_no_mix.html"),
# )

# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--ignore-mt10",
# "--result-set",
# "primitive-no-obs",
# "--out-file",
# Out("success_rates_primitive-no-obs.html"),
# )

# cmd(
# "python",
# "src/plot_tasks_at_success_rate.py",
# "--result-set",
# "language-world",
# "--out-file",
# Out("success_rates_language-world-all.html"),
# )

# cmd(
# "python",
# "src/write_v0_results.py",
# "--oneshot-success-out",
# Out("cond_agent_v0_success_rate_one_shot.json"),
# "--zeroshot-success-out",
# Out("cond_agent_v0_success_rate_zero_shot.json"),
# )
# cmd(
# "python",
# "src/rand_lang_agent.py",
# "--out-file",
# Out("random_language_agent_results.json"),
# )

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

# for env_name in MT50_ENV_NAMES:
# cmd(
# "python",
# "src/render_policy.py",
# "--env-name",
# env_name,
# "--out-file",
# Out(f"render_policy/universal_policy/{env_name}_universal-policy.mp4"),
# extra_outputs=[
# Out(f"render_policy/universal_policy/{env_name}_universal-policy.gif")
# ],
# )

# cmd(
# "python",
# "src/diff_agent.py",
# "--out-success",
# Out("diff-agent_success.json"),
# "--out-avg-reward",
# Out("diff-agent_avg-reward.json"),
# "--render-output-dir",
# Out("render_policy/diff_agent/"),
# )

# cmd(
# "python",
# "src/diff_agent.py",
# "--plan-file",
# "mt50_plans_projected.py",
# "--out-success",
# Out("diff-agent-proj_success.json"),
# "--out-avg-reward",
# Out("diff-agent-proj_avg-reward.json"),
# "--render-output-dir",
# Out("render_policy/diff_agent_proj/"),
# )

# cmd(
# "python",
# "src/evaluator_agent.py",
# "zeroshot",
# "--language-space-mixing=no",
# "--plan-file",
# "mt50_plans_v0.py",
# "--out-file",
# Out("cond_agent_v0_results_no_mix.json"),
# warmup_time=30,
# )

# if psutil.virtual_memory().percent <= 15:
# cmd(
# "python",
# "src/evaluator_agent.py",
# "zeroshot",
# "--plan-file",
# "mt50_plans_v1.py",
# "--out-file",
# Out("cond_agent_v1_zeroshot.ndjson"),
# warmup_time=600,
# )

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

# for env_name in MT40_ENV_NAMES:
# cmd(
# "python",
# "src/mlp_agent.py",
# "fewshot",
# "--target-env",
# env_name,
# "--use-noise",
# "no",
# "--out-file",
# Out(f"mlp_agent_v1_fewshot-{env_name}-no-noise.ndjson"),
# warmup_time=60,
# )

# for env_name in MT40_ENV_NAMES:
# cmd(
# "python",
# "src/mlp_agent.py",
# "real-oneshot",
# "--target-env",
# env_name,
# "--use-noise",
# "no",
# "--out-file",
# Out(f"mlp_agent_v1_real_oneshot-{env_name}-no-noise-full.ndjson"),
# warmup_time=20,
# )

# for env_name in MT40_ENV_NAMES:
#     cmd(
#         "python",
#         "src/mlp_agent.py",
#         "real-oneshot",
#         "--target-env",
#         env_name,
#         "--use-noise",
#         "yes",
#         "--out-file",
#         Out(f"mlp_agent_v2_real_oneshot-{env_name}-noise-full.ndjson"),
#         ram_gb=12,
#     )

# cmd(
# "python",
# "src/evaluator_agent.py",
# "zeroshot",
# "--plan-file",
# "mt50_plans_v1.py",
# "--use-noise",
# "no",
# "--out-file",
# Out(f"cond_agent_v1_zeroshot-no-noise.ndjson"),
# warmup_time=60,
# )

# cmd(
# "python",
# "src/mlp_agent.py",
# "zeroshot",
# "--use-noise=no",
# "--out-file",
# Out(f"mlp_agent_v1_zeroshot-no-noise.ndjson"),
# warmup_time=60,
# )

# cmd(
# "python",
# "src/mlp_agent.py",
# "zeroshot",
# "--use-noise=yes",
# "--out-file",
# Out(f"mlp_agent_v1_zeroshot-noise.ndjson"),
# warmup_time=60,
# )

# cmd(
# "python",
# "src/evaluator_agent.py",
# "zeroshot",
# "--plan-file=mt50_plans_v1.py",
# "--use-noise=no",
# '--give-obs-to-learned-controller=no',
# "--out-file",
# Out(f"cond_agent_v1_zeroshot-naive-no-primitive-obs.ndjson"),
# warmup_time=60,
# )

# cmd(
# "python",
# "src/train_evaluator.py",
# "--out-file",
# Out(f"evaluator_params.pkl"),
# warmup_time=60,
# )

# cmd(
# "python",
# "src/evaluator_agent.py",
# "zeroshot",
# "--plan-file=mt50_plans_v2_from_demonstrations.py",
# "--use-noise=no",
# "--out-file",
# Out(f"cond_agent_v2_zeroshot.ndjson"),
# warmup_time=60,
# )

# cmd(
# "python",
# "src/evaluator_agent.py",
# "zeroshot",
# "--plan-file=mt50_plans_v2_unscored.py",
# "--use-noise=no",
# "--out-file",
# Out(f"cond_agent_v2_zeroshot_unscored.ndjson"),
# warmup_time=60,
# )

# cmd(
# "python",
# "src/evaluator_agent.py",
# "zeroshot",
# "--plan-file=mt50_plans_v2_from_demonstrations.py",
# "--use-noise=yes",
# "--out-file",
# Out(f"cond_agent_v2_zeroshot-noise.ndjson"),
# warmup_time=60,
# )

# cmd(
# "python",
# "src/evaluator_agent.py",
# "zeroshot",
# "--plan-file=mt50_plans_v2_unscored.py",
# "--use-noise=yes",
# "--out-file",
# Out(f"cond_agent_v2_zeroshot_unscored-noise.ndjson"),
# warmup_time=60,
# )
