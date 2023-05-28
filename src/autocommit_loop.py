#!/usr/bin/env python3
from subprocess import run
import time

while True:
    run(["git", "add", "data"], check=False)
    run(["git", "commit", "-m", "Add results"], check=False)
    run(["git", "push"], check=False)
    time.sleep(600)
