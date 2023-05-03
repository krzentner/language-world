

The steps for the `hammer` task are:

1. Put gripper above the hammer
2. Grab the hammer with the gripper
3. Move the hammer over the nail
4. Drop the hammer on the nail

The code to perform the task is:

```
# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Grab the hammer with the gripper
    #  3. Move the hammer over the nail
    #  4. Drop the hammer on the nail
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")
    # As long as the gripper isn't around the hammer, grab it.
    if check("the robot's gripper is not around hammer and the robot's gripper is open"):
        robot.grab("hammer")
    # If the hammer is roughly aligned with the nail as seen from above, move
    # the hammer over the nail
    if check("the hammer is aligned with the nail and the hammer is not above the nail"):
        robot.move("hammer above the nail")
    # If the hammer is above the nail, drop it on the nail.
    if check("the hammer is above the nail"):
        robot.drop("hammer on nail")
```