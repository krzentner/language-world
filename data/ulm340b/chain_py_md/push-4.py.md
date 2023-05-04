

And then write an if-statement that performs a check and makes sure that the first
check, ``the robot's gripper is near the puck'', is true:

```
# push: slide the puck to the target location
def push(robot):
    # We need to be sure the robot's gripper is near the puck before we start
    # pushing.
    if check("the robot's gripper is near the puck"):
```

Once the gripper is near the puck, we can try sliding the puck by just moving
the gripper forward:

```
# push: slide the puck to the target location
def push(robot):
    # We need to be sure the robot's gripper is near the puck before we start
    # pushing.
    if check("the robot's gripper is near the puck"):
        robot.move("gripper forward")
```

To check that the puck has moved to the target location, we just need to check
that it is near the goal, and not left of the goal:

```
# push: slide the puck to the target location
def push(robot):
    # We need to be sure the robot's gripper is near the puck before we start
    # pushing.
    if check("the robot's gripper is near the puck"):
        robot.move("gripper forward")
        # As long as the puck isn't left of the target, keep moving it.
        if check("the puck is near the target and not left of the target"):
            robot.move("gripper forward")
```

We're now done with the `push` task. The last thing to do is run our code!
Begin with this code:

```
robot = get_sim_robot()
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
    if check("the robot's gripper is vertically aligned