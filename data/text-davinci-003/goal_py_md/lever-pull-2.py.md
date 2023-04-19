

The first step is to put the gripper below the lever. We can do this by moving the gripper to a point the same height below the lever.

```
# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper below the lever
    #  2. Pull up the lever
    # First, put the gripper below the lever.
    if check("the robot's gripper is not below the lever"):
        robot.move_gripper("below the lever", close_gripper=True)
```

Next we can pull up the lever by closing the gripper and applying an upwards force.

```
# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper below the lever
    #  2. Pull up the lever
    # First, put the gripper below the lever.
    if check("the robot's gripper is not below the lever"):
        robot.move_gripper("below the lever", close_gripper=True)
    # If the gripper is below the lever and closed, apply an upwards force to pull up the lever.
    if check("the robot's gripper is below the lever and the robot's gripper is closed"):
        robot.move_gripper("upwards")

```