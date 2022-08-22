import clize
import plotly.graph_objects as go
from run_utils import str_list
from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES
import os
import json
import sys


def plot_tasks_auc(data, filename, title="Success Rate", x_label="Success Rate"):
    fig = go.Figure()
    for (exp_name, perf) in data.items():
        tasks_by_success_rate = sorted(
            [(p, env_name) for (env_name, p) in perf.items()]
        )
        env_names = [env_name for (p, env_name) in tasks_by_success_rate]
        N_TASKS = len(env_names)
        y = [N_TASKS]
        x = [0.0]
        text = [",<br>".join(env_names)]
        for i in range(N_TASKS):
            if i > 0 and tasks_by_success_rate[i - 1][0] == tasks_by_success_rate[i][0]:
                continue
            x.append(tasks_by_success_rate[i][0])
            y.append(N_TASKS - i)
            text.append(",<br>".join(env_names[i:]))

        fig.add_trace(go.Scatter(x=x, y=y, text=text, name=exp_name, line_shape="vh"))
        fig.update_yaxes(range=(0, N_TASKS * 1.1), zeroline=True)
    fig.update_layout(title=title, yaxis_title="Number of Tasks", xaxis_title=x_label)
    fig.write_html(filename)
    return fig


def load_result_files(filenames, metric='SuccessRate'):
    perf = {}
    for filename in filenames:
        try:
            try:
                with open(os.path.expanduser(filename)) as f:
                    lines = f.readlines()
                for line in lines:
                    print(filename, file=sys.stderr)
                    data = json.loads(line)
                    for env_name in MT50_ENV_NAMES:
                        key = f'{env_name}/{metric}'
                        if key in data and data[key] > perf.get(key, 0):
                            perf[env_name] = data[key]
            except json.decoder.JSONDecodeError:
                with open(os.path.expanduser(filename)) as f:
                    data = json.load(f)
                    for env_name in MT50_ENV_NAMES:
                        key = f'{env_name}/{metric}'
                        if key in data and data[key] > perf.get(key, 0):
                            perf[env_name] = data[key]
        except FileNotFoundError as exc:
            print(exc, file=sys.stderr)
    return perf


def run(
    *,
    title=None,
    in_file: clize.parameters.multi() = None,
    label: clize.parameters.multi() = None,
    ignore_mt10: bool = False,
    out_file
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
        data = success_rate_results()

    if ignore_mt10:
        from sample_utils import MT10_ENV_NAMES

        for perf in data.values():
            for env_name in MT10_ENV_NAMES:
                if env_name in perf:
                    del perf[env_name]

    plot_tasks_auc(
        data,
        out_file,
        title=title,
    )


def success_rate_results():
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
    data = {
        "CondAgent One Shot (v0 prompt)": one_shot,
        "CondAgent Zero Shot (v0 prompt)": zero_shot,
        # "BC One Shot (WIP)": nabc_one_shot,
        "CondAgent Zero Shot (v0 prompt, No Language Mix, WIP)": zero_shot_no_language_mix,
        "EditDistanceAgent (v0 prompt)": diff_agent,
        "PaLM Chosen Primitives (v1 prompt)": diff_agent_proj,
        "CondAgent Zero Shot (v1 prompt)": load_result_files(
                ['~/exp_data/cond_agent_v1_results.json']),
        "CondAgent One Shot (v1 prompt)": load_result_files(
                [f'~/exp_data/cond_agent_v1_fewshot-{env_name}.json'
                 for env_name in MT50_ENV_NAMES]),
    }
    return data


if __name__ == "__main__":
    clize.run(run)
