
    if check("the robot's gripper is not above button and the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above button and the robot's gripper is not horizontally aligned with button"):
        robot.slide("into button")
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button")

# peg-insert-back: grab the peg and insert it into the hole from above
def peg_insert_back(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.grab("peg")
    if check("the robot's gripper is around peg and peg is not horizontally aligned with hole"):
        robot.slide("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# lever-pull: pull the lever down
def lever_pull(robot):
    if check("the robot's gripper is not forward aligned with lever and the robot's gripper is not above lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is near lever"):
        robot.grab("lever")
    if check("the robot's gripper is vertically aligned with lever"):
        robot.pull("lever down")

# _action(robot):
#     if check():
#         robot.
#     if check():
#         robot.
#     if check():
#         robot.
[eod] [code]#!D:\python\test\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==39.1.0','console_scripts','easy_install'
__requires__ = 'setuptools==39.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('setuptools==39.1.0', 'console_scripts'