

In this task, you will have to line up the gripper with the stick so you can grab it, move the stick to the thermos, then move the stick and thermos to the target location.

Steps:
  1. Put gripper above stick
  2. Drop gripper around stick
  3. Put stick near thermos
  4. Push stick to the target location

To do this, we will first need to put the gripper above the stick.
Then, we'll need to drop the gripper around the stick.
Next, we'll move the stick to the thermos, and finally, move both the stick and the thermos to the target location.

```
# Tasks to perform:
door_open(robot)
stick_push(robot)
```
"""


# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer