

The steps for this task are:

1. Put gripper above the mug handle
2. Drop gripper around mug handle
3. Close gripper around mug handle
4. Move mug to the target location

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug handle
    #  4. Move mug to the target location
    # To begin the task, we need to put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.put("gripper above mug handle")
    # Once the gripper is lined up, we can drop the gripper around the mug handle.
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is not around mug handle"):
        robot.put("gripper around mug handle")
    # Now the gripper is around the mug handle, so we can close it to grab the mug.
    if check("the robot's gripper is around mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    # If the mug is still below the gripper, we're ready to move it.
    if check("the robot's gripper is above mug handle and the robot's gripper is closed"):
        robot.place("mug at target location")
```