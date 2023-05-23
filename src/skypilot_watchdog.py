#!/usr/bin/env python3
import argparse
import time
import re
from subprocess import run, PIPE
import sys

def parse_args():
    parser = argparse.ArgumentParser("doexp skypilot wrapper")
    parser.add_argument("--task-file", required=True)
    parser.add_argument("-o", "--out-file", action="append")
    return parser.parse_args()

def main():
    args = parse_args()
    # Autostop after four hours, manually stop immediately once downloads are done
    launch_proc = run(
            ["sky", "launch", "--yes", "--idle-minutes-to-autostop=240", args.task_file],
        capture_output=True, check=True, text=True)
    output = launch_proc.stdout
    try:
        cluster_name = re.findall(r"To log into the head VM:.*ssh[^\s]* ([A-z0-9-]+)", output)[0]
        job_id = re.findall(r"Job submitted with Job ID: ([0-9]+)", output)
        job_return_codes_crashed = re.findall(r"Job [0-9]+ failed with return code list:.* \[([^0-9]+)", output)
        job_succeeded = "Job finished (status: SUCCEEDED)" in output
        print(launch_proc.stdout)
        print(launch_proc.stderr)
        print("job_id:", job_id)
        print("cluster_name:", cluster_name)
        print("job_return_codes_crashed:", job_return_codes_crashed)
        print("job_succeeded:", job_succeeded)
        if job_succeeded:
            for out_file in args.out_file:
                run(["rsync", "-Pavz", f"{cluster_name}:/home/gcpuser/sky_workdir/{out_file}", out_file])
    finally:
        run(["sky", "down", "--yes", cluster_name])
    if not job_succeeded:
        sys.exit(int(job_return_codes_crashed[0]))

if __name__ == '__main__':
    main()
