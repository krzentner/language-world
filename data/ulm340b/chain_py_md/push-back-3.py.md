

Please finish the program so that it performs the task.
Here's what this task looks like:

```
# push-back: slide the puck backwards to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Slide the puck backwards
    # Put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # Drop the gripper around the puck.
    if check("the robot's gripper is not around the puck"):
        robot.drop("gripper around puck")
    # Drop the gripper around the puck.
    if check("the robot's gripper is around the puck and the puck is below the robot's gripper"):
        robot.push("the puck away")
```

If you make a mistake and would like to start over, type `reset`.
If you get stuck, type `hint` and I'll start you off with some code,
or type `solution` and I'll show you my entire solution.



### Test 2

```
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
    # because of the angle of the robot