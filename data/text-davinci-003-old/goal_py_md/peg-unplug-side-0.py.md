

Steps:
1. Put the gripper forward of the peg
2. Grab the peg with the gripper
3. Pull the peg out of the hole

```
# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    # Steps:
    #  1. Put the gripper forward of the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out of the hole
    # First, move the gripper forward of the peg.
    if check("the robot's gripper is not forward aligned with the peg"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # Once the gripper is in front of the peg, grab it with the gripper.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("left of the peg")
    # Now that the gripper is around the peg, pull it out of the hole.
    if check("the robot's gripper is left of the peg"):
        robot.move_gripper("right of the peg")
```