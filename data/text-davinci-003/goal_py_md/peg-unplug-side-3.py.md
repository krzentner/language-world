

Then add code:

```
# peg-unplug-side: grab the peg and pull the it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper to the left of the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg sideway out of the hole 
    # First, put the gripper to the left of the peg so that we can grab it when
    # we're ready to pull.
    if check("the robot's gripper is not to the left of the peg"):
        robot.move_gripper("to the left of the peg")
    # If the peg becomes right of the gripper, we should move the gripper back
    # to the left of the peg.
    # Because the peg is a long object, we should check if the peg is lined up
    # with the gripper from the back instead of around it.
    if check("peg is not right of the robot's gripper and peg is not rear aligned with the robot's gripper"):
        robot.move_gripper("rear aligned with the peg", close_gripper=True)
    # Once the gripper has the peg trapped, pull the peg to the side to unplug
    # it from the hole.
    if check("the robot's gripper is rear aligned with the peg"):
        robot.move_gripper("to the right of the hole")
```