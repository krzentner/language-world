

If you aren't familiar with Python, use the following templates for each line:

```
#    If [condition]:
#        robot.[function]([arguments])
```

If you ARE familiar with Python, use the following templates for each line:

```
    if [condition]:
        robot.[function]([arguments])
```

Make sure you put a blank line after the `def` line for the function definition.

After writing this program, please continue below.

**Please keep in mind that you have an overall time limit.
If you spend too long on one task you will miss the later tasks.**
"""

# peg-unplug-side: grab the peg and pull the it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out sideways
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not right of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("left of the peg", close_gripper=True)


# peg-unplug-top: grab the peg and pull the it out from the top
def peg_unplug_top(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out upwards
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("left of the peg", close_gripper=True)
    # Once the gripper is near the peg, we can grab it by closing the gripper.
