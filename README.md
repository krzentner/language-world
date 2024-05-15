# Experiment Code of Conditionally Combining Robot Skills using Large Language Models

All experiments are listed by exps.py, and can be shown in expanded form using `python src/doexp.py --dry-run exps.py` (or run using that script without `--dry-run`).
Experiment results are stored in [`data`](data), including all generated plans.

The main PCBC code is in [src/cond_agent.py](src/cond_agent.py) and descriptor conditioning is in [src/mlp_agent.py](src/mlp_agent.py).
