

You can move the robot's gripper with the command:

```
robot.move_gripper("instruction for the robot's gripper")
```

This will move the gripper based on the given instructions. If the gripper is
already following the instruction, the command will do nothing. If you would
like the command to move the gripper even if it's already following the
instruction, set `force=True` like so:

```
robot.move_gripper("instruction for the robot's gripper", force=True)
```

Your `soccer` function can use a few of the functions shown above. For example,
the function `robot.move_gripper` has been defined to make it easier for the
robot to move its gripper.

I will also be giving you a new function, `check`, that returns True if a
condition is met:

```
if check("the robot's gripper is around ball"):
    robot.move_gripper("vertically aligned with ball")
```

You can define a new function if you want.
"""
# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into soccer ball
    #  3. Slide soccer ball to goal

    # First, put the gripper roughly above the soccer ball.
    if check("the robot's gripper is not vertically aligned with soccer ball and the robot's gripper is not near soccer ball"):
        robot.move_gripper("vertically aligned with soccer ball")
    # If the gripper is above the soccer ball and not near it, move the gripper
    # down to the soccer ball.
    if check("the robot's gripper is vertically aligned with soccer ball and the robot's gripper is not near soccer ball"):
        robot.move_gripper("vertically aligned with soccer ball", force=True)
    # If the gripper is above the soccer ball and near it, we've probably trapped
    # the soccer ball and can slide it to the target location.
    if check("the robot's gripper is near soccer ball"):
        robot.move_gripper("vertically aligned with the target location")
[eod] [code]#!D:\github\PycharmProjects\django_project\myenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==10.0.1','console_