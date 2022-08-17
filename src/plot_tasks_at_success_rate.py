import clize
import plotly.graph_objects as go


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


def run(*, title=None, in_file=None, out_file):
    if in_file is None:
        title = "CondAgent v0 Success Rates"
        data = condagent_v0_mt50_results()
    else:
        assert title
        import json
        with open(in_file) as f:
            data = json.load(f)
    plot_tasks_auc(
        data,
        out_file,
        title=title,
    )

def condagent_v0_mt50_results():
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
    data = {"One Shot": one_shot, "Zero Shot": zero_shot}
    return data

if __name__ == "__main__":
    clize.run(run)
