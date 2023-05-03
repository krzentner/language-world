

The steps for hammering a nail with a robot's gripper would be:

1. Put gripper above the nail
2. Put gripper around the hammer handle
3. Close gripper around hammer handle
4. Move robot to above the nail, holding the hammer
5. Lower the grip to the nail
6. Raise the grip back up

Begin by placing the gripper roughly above the nail, so that the robot does not bump the nail while trying to grab the hammer.

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Put gripper above the nail
    #  2. Put gripper around the hammer handle
    #  3. Close gripper around hammer handle
    #  4. Move robot to above the nail, holding the hammer
    #  5. Lower the grip to the nail
    #  6. Raise the grip back up

    # First, put the gripper roughly above the nail, so that we don't bump it while
    # trying to grab the hammer.
    if check("the robot's gripper is not above the nail"):
        robot.move_gripper("above the nail")
```

Then, if the gripper is not around the hammer handle, move the gripper near the hammer handle so it can grab it.

```
    # Then, if the gripper is not around the hammer handle, move the gripper
    # near the hammer handle so it can grab it.
    if check("the robot's gripper is not around the hammer handle and the robot's gripper is open"):
        robot.move_gripper("near the hammer handle", close_gripper=True)
```

If the gripper is near the hammer handle, we can probably grab it by closing the gripper.

```
    # If the gripper is near the hammer handle, we can probably grab it by 
    # closing the gripper.
    if check("the robot's gripper is above the hammer handle and the robot's gripper is closed"):
        robot.move_gripper("above the nail")
```

Once the gripper is holding the hammer, move the robot to above the nail and lower the robot's grip to the nail.

```
    # Once the gripper is holding the hammer, move the robot to above the nail and
    # lower the robot's grip to the nail.
    if check("the robot's gripper is above the nail and the robot's gripper is closed"):
        robot.move_gripper("above the nail")
```

When the robot's grip is