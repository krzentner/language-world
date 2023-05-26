from subprocess import run
import time

while True:
    run(["sky", "autostop", "--yes", "--all", "--idle-minutes", "20", "--down"], check=False)
    time.sleep(600)
