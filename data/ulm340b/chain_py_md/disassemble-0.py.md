

and then put in the correct commands to make `check` return `True`.
"""

"""
# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Line up the wrench with the robot's gripper from above
    #  2. Drop the gripper around the wrench
    #  3. Pull the wrench off
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is vertically aligned with wrench and the robot's gripper is not around wrench"):
        robot.drop("gripper around wrench")
    if check("the robot's gripper is vertically aligned with wrench and the robot's gripper is around wrench"):
        robot.pull("wrench away from peg")
"""

# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Line up the wrench with the robot's gripper from above
    #  2. Drop the gripper around the wrench
    #  3. Pull the wrench off
    if check("the wrench is not vertically aligned with robot's gripper"):
        robot.put("gripper above wrench")
    if check("the wrench is vertically aligned with the robot's gripper and the robot's gripper is not around wrench"):
        robot.drop("gripper around wrench")
    if check("the wrench is vertically aligned with the robot's gripper and the robot's gripper is around wrench"):
        robot.pull("wrench away from peg")

"""
Your code should give a list of the instructions to run:

- `put` the robot's gripper above the wrench
- `drop` the robot's gripper around the wrench
- `pull` the wrench away from the peg
"""

"""
Your code should give a list of the instructions to run:

- `put` the robot's gripper above the wrench
- `drop` the robot's gripper around the wrench
- `pull` the wrench away from the peg
"""

"""
Your code should give a list of the instructions to run:

- `put` the robot's gripper above the wrench
- `drop` the robot's gripper around the wrench
- `pull` the wrench away from the peg
"""

"""
Your code should give a list of the instructions to run:
