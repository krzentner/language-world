from typing import Dict, List
import clize
import plotly.graph_objects as go
from run_utils import str_list
from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES
from tqdm import tqdm
import warnings
import re
import os
import json
import sys


def plot_tasks_auc(data, filename, title="Success Rate", x_label="Success Rate"):
    fig = go.Figure()
    N_TASKS = 40
    for exp_name, perf in data.items():
        env_names = list(perf.keys())
        if len(env_names) > N_TASKS:
            N_TASKS = len(env_names)

        envs_at_success_rate = {}
        for env_name, p in perf.items():
            p = int(100 * p)
            if p not in envs_at_success_rate:
                envs_at_success_rate[p] = [env_name]
            else:
                envs_at_success_rate[p].append(env_name)

        y = [len(env_names)]
        x = [0.0]
        text = [",<br>".join(env_names)]
        envs_remaining = y[0]
        for p, env_names_at_p in sorted(envs_at_success_rate.items()):
            y.append(envs_remaining * N_TASKS / (len(env_names)))
            envs_remaining -= len(env_names_at_p)
            x.append(p)
            text.append(",<br>".join(env_names_at_p))

        # for i in range(len(env_names)):
        # if i > 0 and tasks_by_success_rate[i - 1][0] == tasks_by_success_rate[i][0]:
        # continue
        # x.append(tasks_by_success_rate[i][0])
        # y.append(len(env_names) - i)
        # if i + 1 == len(env_names):
        # text.append(",<br>".join(env_names[last_i:]))
        # else:
        # text.append(",<br>".join(env_names[last_i:i]))
        # last_i = i

        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                text=text,
                name=exp_name,
                line_shape="vh",
            )
        )
    fig.update_yaxes(range=(0, N_TASKS * 1.1), zeroline=True)
    fig.update_layout(
        title=title,
        yaxis_title="Number of Tasks",
        xaxis_title=x_label,
        template="simple_white",
    )
    fig.write_html(filename)
    fig.write_image(filename.replace(".html", ".svg"))
    fig.write_image(filename.replace(".html", ".pdf"))
    return fig


def load_result_file(filename, metric="SuccessRate", max_t=True):
    perf = {}
    with open(os.path.expanduser(filename)) as f:
        data = json.load(f)
        for env_name in MT50_ENV_NAMES:
            key = f"{env_name}/{metric}"
            if key in data and (not max_t or data[key] > perf.get(env_name, -1)):
                perf[env_name] = data[key]
    return perf


def load_result_files(filenames, metric="SuccessRate", n_evals=None, max_t=True):
    perf = {}
    for filename in filenames:
        try:
            with open(os.path.expanduser(filename)) as f:
                lines = f.readlines()
            if n_evals is not None:
                assert (
                    len(lines) >= n_evals
                ), f"{filename} does not contain enough evals"
                lines = lines[:n_evals]
            for line in lines:
                data = json.loads(line)
                for env_name in MT50_ENV_NAMES:
                    key = f"{env_name}/{metric}"
                    if key in data and (
                        not max_t or data[key] > perf.get(env_name, -1)
                    ):
                        perf[env_name] = data[key]
        except FileNotFoundError as exc:
            if n_evals is not None:
                raise exc
            else:
                print(exc, file=sys.stderr)
    return perf


def merge_result_files(result_filenames: List[str]) -> Dict[str, (float, str)]:
    perf = {}
    for filename in result_filenames:
        with open(filename) as f:
            if filename.endswith(".json"):
                data = json.load(f)
            elif filename.endswith(".ndjson"):
                content = f.read()
                objects = re.split(r"\n{", content)
                data = json.loads(objects[0])
            else:
                warnings.warn(f"Could not load file: {filename}")
                data = {}
        for k, v in data.items():
            if k not in perf or v > perf[k][0]:
                perf[k] = (v, filename)
    return perf


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

MODEL_SHORT_NAME = {
    "text-davinci-003": "GPT 3",
    "gpt-3.5-turbo": "GPT 3.5",
    "ulm340b": "PaLM 2",
    "codepoet24b": "PaLM Code",
}

GOOGLE_LLMS = [
    "ulm340b",
    # "codepoet24b",
]


def plot_llm_scripted_skill_evals():
    performances = {}
    for plan_enc in tqdm(PLAN_ENCODINGS):
        for model in GPT3_ENGINES + GPT_CHAT_MODELS + GOOGLE_LLMS:
            perf = merge_result_files(
                [
                    f"data/{model}/{plan_enc}/{task}-{i}-perf.json"
                    for i in range(LLM_ATTEMPTS)
                    for task in MT50_ENV_NAMES
                ]
            )
            performances[f"{MODEL_SHORT_NAME[model]}/{plan_enc}"] = {
                k: v[0] for k, v in perf.items()
            }
    plot_tasks_auc(performances, f"data/scripted_skills.html")
    best_perf = {
        "PaLM 2/chain_py": performances["PaLM 2/chain_py"],
        "GPT 3.5/chain_py": performances["GPT 3.5/chain_py"],
        "GPT 3/basic_py": performances["GPT 3/basic_py"],
    }
    plot_tasks_auc(best_perf, f"data/scripted_skills_best.html")
    palm2_perf = {}
    for plan_enc in tqdm(PLAN_ENCODINGS):
        model = "ulm340b"
        key = f"{MODEL_SHORT_NAME[model]}/{plan_enc}"
        palm2_perf[key] = performances[key]
    plot_tasks_auc(palm2_perf, f"data/scripted_skills_palm2.html")


def run(
    *,
    title=None,
    in_file: clize.parameters.multi() = None,
    label: clize.parameters.multi() = None,
    ignore_mt10: bool = False,
    max_t: bool = True,
    assume_mt10: bool = False,
    result_set: str = "all",
    out_file,
):
    if in_file:
        assert title
        data = {}
        assert len(in_file) == len(label)
        for lab, filename in zip(label, in_file):
            import json

            with open(filename) as f:
                data[lab] = json.load(f)
    else:
        title = "Success Rates"
        data = success_rate_results(result_set, max_t)

    assert not ignore_mt10 or not assume_mt10
    if ignore_mt10:
        from sample_utils import MT10_ENV_NAMES

        for perf in data.values():
            for env_name in MT10_ENV_NAMES:
                if env_name in perf:
                    del perf[env_name]
    elif assume_mt10:
        from sample_utils import MT10_ENV_NAMES

        for perf in data.values():
            for env_name in MT10_ENV_NAMES:
                perf[env_name] = 1.0

    plot_tasks_auc(
        data,
        out_file,
        title=title,
    )


def success_rate_results(result_set, max_t):
    one_shot = {
        "assembly": 1.0,
        "basketball": 0.0,
        "bin-picking": 0.0,
        "box-close": 0.0,
        "button-press-topdown": 1.0,
        "button-press-topdown-wall": 1.0,
        "button-press": 1.0,
        "button-press-wall": 1.0,
        "coffee-button": 1.0,
        "coffee-pull": 1.0,
        "coffee-push": 0.64,
        "dial-turn": 1.0,
        "disassemble": 0.0,
        "door-close": 0.0,
        "door-lock": 0.7,
        "door-open": 1.0,
        "door-unlock": 1.0,
        "hand-insert": 0.82,
        "drawer-close": 1.0,
        "drawer-open": 1.0,
        "faucet-open": 1.0,
        "faucet-close": 1.0,
        "hammer": 0.0,
        "handle-press-side": 1.0,
        "handle-press": 1.0,
        "handle-pull-side": 0.0,
        "handle-pull": 0.14,
        "lever-pull": 0.82,
        "peg-insert-side": 0.0,
        "pick-place-wall": 0.0,
        "pick-out-of-hole": 0.0,
        "reach": 0.0,
        "push-back": 0.0,
        "push": 0.36,
        "pick-place": 0.0,
        "plate-slide": 0.72,
        "plate-slide-side": 1.0,
        "plate-slide-back": 0.0,
        "plate-slide-back-side": 0.7,
        "peg-unplug-side": 0.42,
        "soccer": 0.26,
        "stick-push": 1.0,
        "stick-pull": 1.0,
        "push-wall": 0.1,
        "reach-wall": 1.0,
        "shelf-place": 0.0,
        "sweep-into": 0.94,
        "sweep": 0.0,
        "window-open": 1.0,
        "window-close": 1.0,
    }
    zero_shot = {
        "door-open": 1.0,
        "drawer-open": 1.0,
        "assembly": 0.0,
        "basketball": 0.0,
        "button-press-topdown": 1.0,
        "button-press-topdown-wall": 1.0,
        "button-press": 0.0,
        "button-press-wall": 0.0,
        "coffee-button": 1.0,
        "coffee-pull": 0.0,
        "coffee-push": 0.3277310924369748,
        "bin-picking": 0.0,
        "dial-turn": 0.0,
        "disassemble": 0.0,
        "drawer-close": 1.0,
        "faucet-open": 0.0,
        "faucet-close": 1.0,
        "hammer": 0.0,
        "box-close": 0.0,
        "handle-press-side": 1.0,
        "handle-press": 1.0,
        "handle-pull-side": 0.0,
        "handle-pull": 0.0,
        "lever-pull": 0.0,
        "peg-insert-side": 0.0,
        "peg-unplug-side": 0.0,
        "pick-out-of-hole": 0.0,
        "pick-place": 0.33613445378151263,
        "door-lock": 0.8,
        "pick-place-wall": 0.8,
        "plate-slide": 0.0,
        "plate-slide-side": 0.0,
        "plate-slide-back": 0.0,
        "plate-slide-back-side": 0.2,
        "push-back": 0.0,
        "push": 0.0,
        "push-wall": 0.0,
        "reach": 0.0,
        "door-unlock": 1.0,
        "reach-wall": 0.0,
        "shelf-place": 0.0,
        "soccer": 0.3277310924369748,
        "stick-push": 0.0,
        "stick-pull": 0.0,
        "sweep-into": 0.0,
        "sweep": 0.0,
        "window-open": 1.0,
        "window-close": 1.0,
        "hand-insert": 0.33613445378151263,
        "door-close": 0.0,
    }
    diff_agent = {
        "assembly": 0.0,
        "basketball": 0.0,
        "bin-picking": 0.0,
        "box-close": 0.0,
        "button-press-topdown": 1.0,
        "button-press-topdown-wall": 1.0,
        "button-press": 0.0,
        "button-press-wall": 0.0,
        "coffee-button": 1.0,
        "coffee-pull": 0.0,
        "coffee-push": 0.0,
        "dial-turn": 0.0,
        "disassemble": 0.0,
        "door-close": 0.98,
        "door-lock": 0.08,
        "door-open": 0.0,
        "door-unlock": 0.0,
        "hand-insert": 0.0,
        "drawer-close": 1.0,
        "drawer-open": 1.0,
        "faucet-open": 0.35,
        "faucet-close": 0.25,
        "hammer": 0.0,
        "handle-press-side": 1.0,
        "handle-press": 1.0,
        "handle-pull-side": 0.0,
        "handle-pull": 1.0,
        "lever-pull": 1.0,
        "peg-insert-side": 1.0,
        "pick-place-wall": 0.0,
        "pick-out-of-hole": 0.0,
        "reach": 0.0,
        "push-back": 0.0,
        "push": 0.0,
        "pick-place": 0.0,
        "plate-slide": 0.0,
        "plate-slide-side": 0.4,
        "plate-slide-back": 0.0,
        "plate-slide-back-side": 0.0,
        "peg-unplug-side": 0.03,
        "soccer": 0.0,
        "stick-push": 0.0,
        "stick-pull": 0.0,
        "push-wall": 0.0,
        "reach-wall": 0.0,
        "shelf-place": 0.0,
        "sweep-into": 0.01,
        "sweep": 0.0,
        "window-open": 1.0,
        "window-close": 0.0,
    }
    nabc_one_shot = {
        "basketball": 0.1,
        "button-press-topdown": 0.25,
        "coffee-pull": 0.4,
        "door-close": 0.85,
        "door-unlock": 0.75,
        "drawer-open": 0.25,
        "faucet-open": 1,
        "hand-insert": 0,
        "faucet-close": 1,
        "handle-press-side": 0.85,
        "handle-pull-side": 0.5,
        "lever-pull": 0,
        "peg-unplug-side": 0.25,
        "pick-place": 0,
        "plate-slide": 0.5,
        "push": 0.05,
        "shelf-place": 0,
        "push-wall": 0.05,
        "stick-pull": 0.1,
        "sweep-into": 0,
        "window-close": 1,
        "window-open": 0.7,
    }
    diff_agent_proj = {
        "assembly": 0.0,
        "basketball": 0.0,
        "bin-picking": 0.0,
        "box-close": 0.0,
        "button-press-topdown": 1.0,
        "button-press-topdown-wall": 1.0,
        "button-press": 0.0,
        "button-press-wall": 0.0,
        "coffee-button": 0.13,
        "coffee-pull": 0.0,
        "coffee-push": 0.0,
        "dial-turn": 0.0,
        "disassemble": 0.0,
        "door-close": 1.0,
        "door-lock": 0.0,
        "door-open": 0.0,
        "door-unlock": 0.0,
        "hand-insert": 0.0,
        "drawer-close": 1.0,
        "drawer-open": 1.0,
        "faucet-open": 0.29,
        "faucet-close": 0.12,
        "hammer": 0.0,
        "handle-press-side": 1.0,
        "handle-press": 1.0,
        "handle-pull-side": 0.0,
        "handle-pull": 1.0,
        "lever-pull": 0.0,
        "peg-insert-side": 1.0,
        "pick-place-wall": 0.0,
        "pick-out-of-hole": 0.0,
        "reach": 0.0,
        "push-back": 0.0,
        "push": 0.0,
        "pick-place": 0.0,
        "plate-slide": 0.0,
        "plate-slide-side": 0.0,
        "plate-slide-back": 0.0,
        "plate-slide-back-side": 0.0,
        "peg-unplug-side": 0.0,
        "soccer": 0.0,
        "stick-push": 0.0,
        "stick-pull": 0.0,
        "push-wall": 0.35,
        "reach-wall": 0.0,
        "shelf-place": 0.0,
        "sweep-into": 0.0,
        "sweep": 0.0,
        "window-open": 1.0,
        "window-close": 1.0,
    }
    zero_shot_no_language_mix = {
        "reach": 0.2,
        "push": 0.44,
        "pick-place": 0.32,
        "door-open": 1.0,
        "drawer-open": 1.0,
        "drawer-close": 1.0,
        "button-press-topdown": 1.0,
        "peg-insert-side": 0.0,
        "window-open": 1.0,
        "window-close": 1.0,
        "assembly": 0.0,
        "basketball": 0.0,
        "bin-picking": 0.0,
        "box-close": 0.0,
        "button-press-topdown-wall": 1.0,
        "button-press": 0.0,
        "button-press-wall": 0.11764705882352941,
        "coffee-button": 1.0,
        "coffee-pull": 0.0,
        "coffee-push": 0.28,
        "dial-turn": 0.0,
        "disassemble": 0.0,
        "door-close": 0.02,
        "door-lock": 0.0,
        "door-unlock": 0.64,
        "hand-insert": 0.02,
        "faucet-open": 0.62,
        "faucet-close": 0.0,
        "hammer": 0.0,
        "handle-press-side": 0.6,
        "handle-press": 1.0,
        "handle-pull-side": 0.0,
        "handle-pull": 0.42,
        "lever-pull": 0.0,
        "pick-place-wall": 0.14,
        "pick-out-of-hole": 0.0,
        "push-back": 0.0,
        "plate-slide": 0.0,
        "plate-slide-side": 0.1,
        "plate-slide-back": 0.0,
        "plate-slide-back-side": 0.0,
        "peg-unplug-side": 0.0,
        "soccer": 0.18,
        "stick-push": 0.0,
        "stick-pull": 0.0,
        "push-wall": 0.12,
        "reach-wall": 0.2,
        "shelf-place": 0.0,
        "sweep-into": 0.0,
        "sweep": 0.0,
    }
    if result_set == "all":
        data = {
            "CondAgent One Shot (v0 prompt)": one_shot,
            "CondAgent Zero Shot (v0 prompt)": zero_shot,
            # "BC One Shot (WIP)": nabc_one_shot,
            "CondAgent Zero Shot (v0 prompt, No Language Mix, WIP)": zero_shot_no_language_mix,
            "EditDistanceAgent (v0 prompt)": diff_agent,
            "PaLM Chosen Primitives (v1 prompt)": diff_agent_proj,
            "CondAgent Zero Shot (v1 prompt, short run)": load_result_files(
                ["~/exp_data/cond_agent_v1_results.json"], max_t=max_t
            ),
            "CondAgent Zero Shot (v1 prompt)": load_result_files(
                ["~/exp_data2/cond_agent_v1_zeroshot-no-noise.ndjson"], max_t=max_t
            ),
            "CondAgent One Shot (v1 prompt, short run)": load_result_files(
                [
                    f"~/exp_data/cond_agent_v1_fewshot-{env_name}.json"
                    for env_name in MT50_ENV_NAMES
                ],
                max_t=max_t,
            ),
            # "CondAgent One Shot (v1 prompt)": load_result_files(
            # [f'~/exp_data/cond_agent_v1_fewshot-{env_name}.ndjson'
            # for env_name in MT50_ENV_NAMES], max_t=max_t),
            "CondAgent One Shot (v1 prompt)": load_result_files(
                [
                    f"~/exp_data2/cond_agent_v1_fewshot-{env_name}-no-noise.ndjson"
                    for env_name in MT50_ENV_NAMES
                ],
                max_t=max_t,
            ),
            "MLPAgent One Shot (NABC)": load_result_files(
                [
                    f"~/exp_data/mlp_agent_v1_fewshot-{env_name}.ndjson"
                    for env_name in MT50_ENV_NAMES
                ],
                max_t=max_t,
            ),
            "MLPAgent One Shot": load_result_files(
                [
                    f"~/exp_data/mlp_agent_v1_fewshot-{env_name}-no-noise.ndjson"
                    for env_name in MT50_ENV_NAMES
                ],
                max_t=max_t,
            ),
            "Random Primitive Agent": load_result_file(
                "~/exp_data/random_language_agent_results.json", max_t=max_t
            ),
            "Sequential Primitives Agent (v1 prompt)": load_result_file(
                "~/exp_data/uncond_agent-v1-results.json", max_t=max_t
            ),
        }
    elif result_set == "language-world":
        data = {
            "Random Primitive Agent": load_result_file(
                "~/exp_data/random_language_agent_results.json", max_t=max_t
            ),
            "PaLM Primitive Sequence (v1 prompt)": load_result_file(
                "~/exp_data/uncond_agent-v1-results.json", max_t=max_t
            ),
            "PaLM Conditions + Primitives (v1 prompt)": diff_agent_proj,
        }
    elif result_set == "zeroshot":
        data = {
            "CondAgent Zero Shot (goal prompt, ABR)": load_result_files(
                ["~/exp_data/cond_agent_v2_zeroshot.ndjson"], max_t=max_t
            ),
            "CondAgent Zero Shot (v0 prompt, ABR)": zero_shot,
            "CondAgent Zero Shot (v1 prompt, ABR)": load_result_files(
                ["~/exp_data/cond_agent_v1_zeroshot.ndjson"], max_t=max_t
            ),
            # "MLPAgent Zero Shot": load_result_file(
            # '~/exp_data/mlp_agent_v1_zeroshot-no-noise.ndjson', max_t=max_t),
            "Random Primitive Agent": load_result_file(
                "~/exp_data/random_language_agent_results.json", max_t=max_t
            ),
            "PaLM Conditions + Primitives (v1 prompt)": diff_agent_proj,
        }
    elif result_set == "zeroshot-no-noise":
        data = {
            "CondAgent Zero Shot (goal prompt)": load_result_files(
                ["~/exp_data/cond_agent_v2_zeroshot-no-noise.ndjson"], max_t=max_t
            ),
            "CondAgent Zero Shot (v1 prompt)": load_result_files(
                ["~/exp_data/cond_agent_v1_zeroshot-no-noise.ndjson"], max_t=max_t
            ),
            # "MLPAgent Zero Shot": load_result_file(
            # '~/exp_data/mlp_agent_v1_zeroshot.ndjson'),
            "Random Primitive Agent": load_result_file(
                "~/exp_data/random_language_agent_results.json", max_t=max_t
            ),
            "PaLM Conditions + Primitives (v1 prompt)": diff_agent_proj,
        }
    elif result_set == "no-mix":
        data = {
            "CondAgent Zero Shot (v0 prompt, ABR)": zero_shot,
            "CondAgent-argmax Zero Shot (v0 prompt, ABR)": load_result_files(
                ["~/exp_data/cond_agent_v0_results_no_mix.json"], max_t=False
            ),
        }
    elif result_set == "noise-difference":
        data = {
            # "CondAgent Zero Shot (goal prompt)": load_result_files([
            # '~/exp_data/cond_agent_v2_zeroshot.ndjson'
            # ], max_t=max_t),
            # "CondAgent Zero Shot (goal prompt, ABR)": load_result_files([
            # '~/exp_data/cond_agent_v2_zeroshot-noise.ndjson'
            # ], max_t=max_t),
            "CondAgent Zero Shot (v1 prompt)": load_result_files(
                ["~/exp_data/cond_agent_v1_zeroshot-no-noise.ndjson"], max_t=max_t
            ),
            "CondAgent Zero Shot (v1 prompt, ABR)": load_result_files(
                ["~/exp_data/cond_agent_v1_zeroshot.ndjson"], max_t=max_t
            ),
            # "MLPAgent Zero Shot": load_result_file(
            # '~/exp_data/mlp_agent_v1_zeroshot.ndjson'),
            # "Random Primitive Agent": load_result_file(
            # '~/exp_data/random_language_agent_results.json', max_t=max_t),
            # "PaLM Conditions + Primitives (v1 prompt)": diff_agent_proj,
        }
    elif result_set == "primitive-no-obs":
        data = {
            # "CondAgent Zero Shot (goal prompt)": load_result_files([
            # '~/exp_data/cond_agent_v2_zeroshot.ndjson'
            # ], max_t=max_t),
            # "CondAgent Zero Shot (goal prompt, ABR)": load_result_files([
            # '~/exp_data/cond_agent_v2_zeroshot-noise.ndjson'
            # ], max_t=max_t),
            "CondAgent Zero Shot (v1 prompt)": load_result_files(
                ["~/exp_data/cond_agent_v1_zeroshot-no-noise.ndjson"], max_t=max_t
            ),
            # "CondAgent Zero Shot (v1 prompt, ABR)": load_result_files([
            # '~/exp_data/cond_agent_v1_zeroshot.ndjson'
            # ], max_t=max_t),
            "CondAgent Zero Shot (v1 prompt, hidden obs)": load_result_files(
                ["~/exp_data/cond_agent_v1_zeroshot-naive-no-primitive-obs.ndjson"],
                max_t=max_t,
            ),
            # "MLPAgent Zero Shot": load_result_file(
            # '~/exp_data/mlp_agent_v1_zeroshot.ndjson'),
            # "Random Primitive Agent": load_result_file(
            # '~/exp_data/random_language_agent_results.json', max_t=max_t),
            # "PaLM Conditions + Primitives (v1 prompt)": diff_agent_proj,
        }
    elif result_set == "best":
        data = {
            # "PaLM Chosen Primitives (v1 prompt)": diff_agent_proj,
            # "CondAgent Zero Shot (v1 prompt)": load_result_file(
            # '~/exp_data2/tmp/cond_agent_v1_zeroshot-no-noise.ndjson'),
            # "CondAgent Zero Shot (v0 prompt, ABR)": zero_shot,
            "CondAgent Zero Shot (v1 prompt)": load_result_files(
                ["~/exp_data/cond_agent_v1_zeroshot-no-noise.ndjson"], max_t=max_t
            ),
            "CondAgent Zero Shot (v1 prompt, ABR)": load_result_files(
                ["~/exp_data/cond_agent_v1_zeroshot.ndjson"], max_t=max_t
            ),
            # "CondAgent One Shot (v1 prompt)": load_result_files(
            # [f'~/exp_data/cond_agent_v1_fewshot-{env_name}.ndjson'
            # for env_name in MT50_ENV_NAMES], max_t=max_t),
            "CondAgent One Shot (v1 prompt)": load_result_files(
                [
                    f"~/exp_data2/cond_agent_v1_fewshot-{env_name}-no-noise.ndjson"
                    for env_name in MT50_ENV_NAMES
                ],
                max_t=False,
            ),
            # "CondAgent One Shot (v1 prompt, ABR)": load_result_files(
            # [f'~/exp_data2/cond_agent_v1_fewshot-{env_name}.ndjson'
            # for env_name in MT50_ENV_NAMES], max_t=max_t),
            "MLPAgent One Shot": load_result_files(
                [
                    f"~/exp_data/mlp_agent_v1_fewshot-{env_name}-no-noise.ndjson"
                    for env_name in MT50_ENV_NAMES
                ],
                max_t=False,
            ),
            # "MLPAgent True One Shot": load_result_files(
            # [f'~/exp_data/tmp/mlp_agent_v1_real_oneshot-{env_name}-no-noise-full.ndjson'
            # for env_name in MT50_ENV_NAMES], max_t=False),
            "Random Primitive Agent": load_result_file(
                "~/exp_data/random_language_agent_results.json", max_t=max_t
            ),
        }
    return data


if __name__ == "__main__":
    clize.run(run, plot_llm_scripted_skill_evals)
