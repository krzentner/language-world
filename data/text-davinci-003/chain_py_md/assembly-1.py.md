

Then, continue with the following steps:

1. Put gripper above wrench
2. Grab wrench with gripper
3. Put gripper around peg
4. Put wrench around peg
5. Push peg and wrench together

```
# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab wrench with gripper
    #  3. Put gripper around peg
    #  4. Put wrench around peg
    #  5. Push peg and wrench together
    # First, move the gripper so that it is above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # Now, if the wrench is left of the robot's gripper, grab it.
    if check("wrench is left of the robot's gripper and the robot's gripper is not around the wrench"):
        robot.grab("wrench")
    # If the robot's gripper and the wrench are aligned, move the grip to around the peg.
    if check("the robot's gripper is forward aligned with the wrench and the robot's gripper is not around the peg"):
        robot.put("gripper around peg")
    # Now that the gripper is around the peg, line the wrench up with it.
    if check("the robot's gripper is around the peg and the wrench is not horizontally aligned with the peg"):
        robot.align("wrench to peg")
    # Finally, push the peg and wrench together.
    if check("the wrench is horizontally aligned with the peg"):
        robot.push("peg and wrench together")
```