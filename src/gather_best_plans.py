import clize
from plan_encoding import load_plan_file
from constants import (
    MT50_ENV_NAMES,
    LLM_ATTEMPTS,
)
from plot_tasks_at_success_rate import merge_result_files
from plan_encoding import load_plan_file, save, project_plan
from tqdm import tqdm
import json


def gather_best_plans(out_file: str, *, out_encoding: str = "json"):
    model = "ulm340b"
    plan_enc = "chain_py"
    perf = merge_result_files(
        [
            f"data/{model}/{plan_enc}/{task}-{i}-perf.json"
            for i in range(LLM_ATTEMPTS)
            for task in MT50_ENV_NAMES
        ]
    )
    result_to_plan = {
        f"data/{model}/{plan_enc}/{task}-{i}-perf.json": f"data/{model}/{plan_enc}/{task}-{i}.py"
        for i in range(LLM_ATTEMPTS)
        for task in MT50_ENV_NAMES
    }
    merged_plans = {}
    for task, (_, result_file) in perf.items():
        merged_plans[task] = load_plan_file(result_to_plan[result_file], default_task=task)[task]
    save(json.dumps(merged_plans, indent=True), out_file)
    projected_plans = {}
    for task, plan in tqdm(merged_plans.items()):
        projected_plans[task] = project_plan(plan, task)
    save(json.dumps(merged_plans, indent=True), out_file.replace('.json', '-projected.json'))


if __name__ == "__main__":
    clize.run(gather_best_plans)
