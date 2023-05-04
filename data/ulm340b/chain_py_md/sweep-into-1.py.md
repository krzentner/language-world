

Note that the code above only uses the `if check(condition)`
statement, and no other conditional statements.
It also only uses simple English for everything except "robot.some_action()".
Please follow this convention in your program, as we will be reading it.

You can write the program in the space below or paste it here.

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.place("cube at goal")
```

You can also use Python-style comments and syntax,
as long as your comments clearly describe what the code does.
"""


# We start with some comments about the task
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Here are some comments about the steps in the task
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
  