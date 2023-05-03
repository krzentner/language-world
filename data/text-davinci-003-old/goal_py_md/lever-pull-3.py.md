

Next, we want to go about performing the task. The robot has to pull the lever up, so we need to make sure the gripper is in a good position.
First, we need to put the gripper above the lever.

```
# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper above lever 
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("vertically aligned with the lever")
```

Next, we want to make sure the gripper is actually around the lever before we begin pulling.

```
# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper above lever 
    #  2. Drop gripper around lever
    if check("the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever")
```

Finally, we want to pull the lever. We can do this by moving the robot's gripper to the left of the lever.

```
# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper above lever 
    #  2. Drop gripper around lever
    #  3. Pull the lever up
    if check("the robot's gripper is not left of the lever"):
        robot.move_gripper("left of the lever")
```

And that's it! Now the robot should be able to pull the lever up.