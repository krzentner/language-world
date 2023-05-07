from doexp import cmd, FileArg, In, Out, GLOBAL_CONTEXT
from constants import (
    GOOGLE_LLMS,
    MT50_ENV_NAMES,
    MT10_ENV_NAMES,
    LLM_ATTEMPTS,
    GPT3_ENGINES,
    GPT_CHAT_MODELS,
    PLAN_ENCODINGS,
)
import psutil

GLOBAL_CONTEXT.max_concurrent_jobs = 1
GLOBAL_CONTEXT.vm_percent_cap = 90.0

RAM_TINY = 0.3


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
    ram_gb=RAM_TINY,
)

cmd(
    "python",
    "src/extract_json.py",
    In(f"output_no-labels_ulm340b-long-int8.json"),
    FileArg(f"ulm340b/{{plan_enc}}/{{task}}-{{i}}{{ext}}"),
    extra_outputs=[
        Out(f"ulm340b/{plan_enc}/{task}-{i}{plan_ext(plan_enc)}")
        for i in range(LLM_ATTEMPTS)
        for plan_enc in PLAN_ENCODINGS
        for task in MT50_ENV_NAMES
    ],
    warmup_time=10,
    ram_gb=1.0,
    priority=1,
)

# cmd(
#     "python",
#     "src/extract_json.py",
#     In(f"output_no-labels_codepoet_24b_int8.json"),
#     FileArg(f"codepoet24b/{{plan_enc}}/{{task}}-{{i}}{{ext}}"),
#     extra_outputs=[
#         Out(f"codepoet24b/{plan_enc}/{task}-{i}{plan_ext(plan_enc)}")
#         for i in range(LLM_ATTEMPTS)
#         for plan_enc in PLAN_ENCODINGS
#         for task in MT50_ENV_NAMES
#     ],
#     warmup_time=10,
#     ram_gb=1.0,
#     priority=1,
# )


LLM_EVAL_FILES = []
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
                warmup_time=5,
                ram_gb=RAM_TINY,
                priority=2,
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
                warmup_time=10,
                ram_gb=RAM_TINY,
                priority=1,
            )
        for model in GPT3_ENGINES + GPT_CHAT_MODELS + GOOGLE_LLMS:
            for i in range(LLM_ATTEMPTS):
                out_file = f"{model}/{plan_enc}/{task}-{i}-perf.json"
                cmd(
                    "python",
                    "src/scripted_cond_agent.py",
                    f"--task={task}",
                    In(f"{model}/{plan_enc}/{task}-{i}{ext}"),
                    Out(out_file),
                )
                LLM_EVAL_FILES.append(out_file)

cmd(
    "python",
    "src/plot_tasks_at_success_rate.py",
    "plot-llm-scripted-skill-evals",
    Out("scripted_skills.html"),
    extra_inputs=[In(eval_file) for eval_file in LLM_EVAL_FILES],
    ram_gb=RAM_TINY,
    priority=-1,
)

cmd(
    "python",
    "src/gather_best_plans.py",
    Out("ulm340b_best_plans.json"),
    extra_inputs=[In(eval_file) for eval_file in LLM_EVAL_FILES],
    ram_gb=RAM_TINY,
    priority=-1,
)

for seed in range(8):
    cmd(
        "python",
        "src/mlp_agent.py",
        "zeroshot",
        "--out-file",
        Out(f"mlp_agent_zeroshot-results-{seed}.ndjson"),
        f"--seed={seed}",
        ram_gb=40,
        priority=(5, seed, 1),
        warmup_time=30,
    )

    cmd(
        "python",
        "src/cond_agent.py",
        "zeroshot",
        "--plan-file",
        In("ulm340b_best_plans.json"),
        "--out-file",
        Out(f"cond_agent_zeroshot-results-{seed}.ndjson"),
        f"--seed={seed}",
        ram_gb=24,
        priority=(4, seed, 3),
        warmup_time=30,
    )

    cmd(
        "python",
        "src/cond_agent.py",
        "zeroshot",
        "--project-skills=yes",
        "--plan-file",
        In("ulm340b_best_plans.json"),
        "--out-file",
        Out(f"cond_agent_zeroshot-projected-results-{seed}.ndjson"),
        f"--seed={seed}",
        ram_gb=24,
        priority=(4, seed, 3),
        warmup_time=30,
    )

    for task in MT50_ENV_NAMES:
        cmd(
            "python",
            "src/mlp_agent.py",
            "oneshot",
            "--target-task",
            task,
            "--out-file",
            Out(f"mlp_agent_oneshot-results-{task}-{seed}.ndjson"),
            f"--seed={seed}",
            ram_gb=8,
            priority=(4, seed, 3),
            warmup_time=30,
        )

        cmd(
            "python",
            "src/cond_agent.py",
            "oneshot",
            "--target-task",
            task,
            "--plan-file",
            In("ulm340b_best_plans.json"),
            "--out-file",
            Out(f"cond_agent_oneshot-results-{seed}.ndjson"),
            f"--seed={seed}",
            ram_gb=8,
            priority=(4, seed, 2),
            warmup_time=30,
        )

        cmd(
            "python",
            "src/cond_agent.py",
            "oneshot",
            "--project-skills=yes",
            "--target-task",
            task,
            "--plan-file",
            In("ulm340b_best_plans.json"),
            "--out-file",
            Out(f"cond_agent_oneshot-projected-results-{seed}.ndjson"),
            f"--seed={seed}",
            ram_gb=8,
            priority=(4, seed, 2),
            warmup_time=30,
        )

        cmd(
            "python",
            "src/mlp_agent.py",
            "oneshot-no-transfer",
            "--target-task",
            task,
            "--out-file",
            Out(f"mlp_agent_oneshot_no_transfer-results-{task}-{seed}.ndjson"),
            f"--seed={seed}",
            ram_gb=8,
            priority=(4, seed, 0),
            warmup_time=30,
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
