

Then follow the `Steps` and replace the `check` conditions and `move_gripper` instructions in the code examples above to accomplish the task.
For example, in the `check` condition:

```
# Steps:
#  1. Put gripper above the puck
#  2. Push gripper into top of puck
#  3. Slide puck to goal
# If the robot's gripper is not above the puck, we can probably move it above the
# puck.
if check("the robot's gripper is not above puck"):
```

the text `the robot's gripper is not above puck` describes a test for whether the puck is under the robot's gripper, if it is, the code in the `if` block will be run.

In `move_gripper` instructions:

```
# Steps:
#  1. Put gripper above the puck
#  2. Push gripper into top of puck
#  3. Slide puck to goal
# If the puck isn't below the gripper as seen from above, move the gripper
# above the puck.
if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
    robot.move_gripper("vertically aligned with the puck")
```

`vertically aligned with the puck` is a description for the movement to be performed by the robot's gripper.

When done, please write the program in this box:

"""

# Instructions:
# Complete faucet-open:
def faucet_open(robot):

    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Turn faucet open
    # We need to put the gripper above the faucet handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.move_gripper("above faucet handle")
    # Once the gripper is lined up above the faucet handle, we should be able to
    # grab the faucet handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("above faucet handle")
    # Once the gripper is around the faucet handle, we can just turn