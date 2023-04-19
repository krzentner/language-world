

The robot should be able to perform the following steps to disassemble: 
1. Put the gripper above the wrench. 
2. Drop the gripper around the wrench.
3. Pull the wrench off the peg.

```
# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Drop gripper around wrench
    #  3. Pull wrench off peg
    # Put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench", close_gripper=True)
    # If the wrench isn't around the gripper, move the gripper around the wrench.
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is not around the wrench"):
        robot.move_gripper("around the wrench")
    # Now that the gripper is around the wrench, pull the wrench off the peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("left of the peg")
```