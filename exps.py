#!/usr/bin/env -S python3 src/doexp.py
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
from socket import gethostname

HOSTNAME = gethostname()

GLOBAL_CONTEXT.max_concurrent_jobs = 2
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

if HOSTNAME == "sky-control":
    #GLOBAL_CONTEXT.max_concurrent_jobs = 3
    #GLOBAL_CONTEXT.max_concurrent_jobs = 15
    GLOBAL_CONTEXT.max_concurrent_jobs = 30
    #GLOBAL_CONTEXT.max_concurrent_jobs = 0
    #GLOBAL_CONTEXT.max_core_alloc = 350
    #GLOBAL_CONTEXT._vm_percent_cap = 800

for i in range(10):
    cmd(
        "python",
        "src/test_experiment.py",
        "--content", f"Hello {i}!",
        "--out-file", Out(f"test_output{i}.txt"),
        skypilot_template="scripts/skypilot_template.yaml",
        priority=100
    )

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
    priority=10,
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
    priority=10,
)

cmd(
    "python",
    "src/extract_json.py",
    In(f"output_no-labels_codepoet_24b_int8.json"),
    FileArg(f"codepoet24b/{{plan_enc}}/{{task}}-{{i}}{{ext}}"),
    extra_outputs=[
        Out(f"codepoet24b/{plan_enc}/{task}-{i}{plan_ext(plan_enc)}")
        for i in range(LLM_ATTEMPTS)
        for plan_enc in PLAN_ENCODINGS
        for task in MT50_ENV_NAMES
    ],
    warmup_time=10,
    ram_gb=1.0,
    priority=10,
)


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
                priority=9,
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
                priority=9,
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
                    priority=9,
                )
                LLM_EVAL_FILES.append(out_file)

cmd(
    "python",
    "src/plot_tasks_at_success_rate.py",
    "plot-llm-scripted-skill-evals",
    Out("scripted_skills.html"),
    extra_inputs=[In(eval_file) for eval_file in LLM_EVAL_FILES],
    ram_gb=RAM_TINY,
    priority=8,
)

cmd(
    "python",
    "src/gather_best_plans.py",
    Out("ulm340b_best_plans.json"),
    extra_inputs=[In(eval_file) for eval_file in LLM_EVAL_FILES],
    ram_gb=RAM_TINY,
    priority=8,
)

seeds = [1111, 2222, 3333, 4444]
template_c2 = "scripts/skypilot_template.yaml"

# for seed in range(8):
for seed in seeds:
    cmd(
        "python",
        "src/mlp_agent.py",
        "zeroshot",
        "--out-file",
        Out(f"mlp_agent_zeroshot-results-{seed}.ndjson"),
        f"--seed={seed}",
        ram_gb=40,
        priority=(7, -seed, 5),
        warmup_time=30,
        skypilot_template=template_c2
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
        ram_gb=48,
        priority=(7, -seed, 4),
        warmup_time=30,
        skypilot_template=template_c2
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
        ram_gb=48,
        priority=(7, -seed, 4),
        warmup_time=30,
        skypilot_template=template_c2
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
            priority=(7, -seed, 3),
            warmup_time=30,
            skypilot_template=template_c2
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
            Out(f"cond_agent_oneshot-results-{task}-{seed}.ndjson"),
            f"--seed={seed}",
            ram_gb=8,
            priority=(7, -seed, 2),
            warmup_time=300,
            skypilot_template=template_c2
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
            Out(f"cond_agent_oneshot-projected-results-{task}-{seed}.ndjson"),
            f"--seed={seed}",
            ram_gb=8,
            priority=(7, -seed, 2),
            warmup_time=30,
            skypilot_template=template_c2
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
            priority=(6, -seed, 0),
            warmup_time=30,
            skypilot_template=template_c2
        )
