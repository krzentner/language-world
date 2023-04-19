

Steps:
1. Put gripper above wrench
2. Grab wrench with gripper
3. Pull wrench off of the peg

If the robot's gripper is not near the wrench, move it near the wrench.

```
# disassemble: pull the wrench off of the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab wrench with gripper
    #  3. Pull wrench off of the peg
    # If the robot's gripper is not near the wrench, move it near the wrench.
    if check("the robot's gripper is not near the wrench"):
        robot.move_gripper("near the wrench")
    # Once the gripper is near the wrench, grab the wrench by closing the
    # gripper.
    if check("the robot's gripper is near the wrench and the robot's gripper is open"):
        robot.move_gripper("above the wrench", close_gripper=True)
    # If the robot has the wrench, pull it off the peg.
    if check("the robot's gripper is closed and the wrench is facing the peg"):
        robot.move_gripper("away from the peg")
```