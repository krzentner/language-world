

```
# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper over wrench
    #  2. Reach down to the wrench
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # Then, reach down to the wrench.
    if check("the robot's gripper is not near the wrench"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # Finally, pull the wrench off the peg.
    if check("the robot's gripper is near the wrench"):
        robot.move_gripper("above the peg")

```