

The program should be as follows:

```
# disassemble: pull the wrench off the peg
# def disassemble(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around wrench
    #  3. Pull wrench off peg
    # First, put the gripper above the peg so that the wrench is below the
    # gripper.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the wrench isn't around the gripper as seen from below, move the
    # gripper below the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # If the gripper is near the wrench and open, maybe we can grab it by
    # closing the gripper. 
    if check("the robot's gripper is near wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    # We closed the gripper, and the wrench is still near the gripper, so maybe
    # we grabbed it. Try to pull the wrench off the peg. If we didn't grab it,
    # we'll just go back to an earlier step.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.pull("wrench off peg")
```