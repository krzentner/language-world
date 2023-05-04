import clize
import json
from sample_utils import MT50_ENV_NAMES, PLAN_ENCODINGS
import os

LLM_ATTEMPTS = 5


def extract_json(in_file, out_file_pattern):
    with open(in_file) as f:
        data = json.load(f)
    for plan_enc in PLAN_ENCODINGS:
        for task in MT50_ENV_NAMES:
            for i in range(LLM_ATTEMPTS):
                ext = "." + plan_enc.split("_", maxsplit=1)[1].replace("_", ".")
                result = data[f"data/{plan_enc}/{task}{ext}-output-{i}"]
                out_filename = out_file_pattern.format(
                    plan_enc=plan_enc,
                    task=task,
                    i=i,
                    ext=ext,
                )
                os.makedirs(out_filename.rsplit("/", maxsplit=1)[0], exist_ok=True)
                with open(out_filename, "w") as f:
                    print("write to", out_filename)
                    f.write(result)


if __name__ == "__main__":
    clize.run(extract_json)
