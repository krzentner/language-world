

Then add the steps:

```
# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put gripper around the lever
    #  2. Grip lever with gripper
    #  3. Rotate the lever up
    # To start, put the gripper around the lever.
    if check("the robot's gripper is not around the lever"):
        robot.put("gripper around the lever")
    # Now that the gripper is around the lever, grip it.
    if check("the robot's gripper is around the lever and the robot's gripper is open"):
        robot.grab("lever with gripper")
    # Now that we've got a grip on the lever, we can rotate it.
    if check("the robot's gripper is around the lever and the robot's gripper is closed"):
        robot.rotate("lever up")
```