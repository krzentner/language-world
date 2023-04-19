

Then, fill in the Steps section with code:

```
# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    # Steps:
    #  1. Put the gripper forward aligned with the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg sideways
    # First, put the gripper forward aligned with the peg.
    if check("the peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)  
    # Now that the gripper is lined up with the peg, just grab it.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("around the peg")
    # Once the gripper is grabing the peg, we can pull the peg sideways.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("left of the hole")     
```