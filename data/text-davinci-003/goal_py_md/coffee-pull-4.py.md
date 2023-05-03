

 then you can fill in the code:

```
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    # 1. Put gripper above mug handle
    # 2. Drop gripper around mug handle
    # 3. Close gripper around mug handle
    # 4. Pull mug to target location
    # First, put the gripper roughly above mug handle, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # If the gripper isn't around the mug handle, put it around the mug handle.
    if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # If the gripper is around the mug handle, maybe we can grab it.
    if check("the robot's gripper is around the mug handle and the robot's gripper is closed"):
        robot.move_gripper("horizontally aligned with the mug handle")
    # If the gripper is grabbing the mug, we can just pull the mug to the target location.
    if check("the robot's gripper is horizontally aligned with the mug handle"):
        robot.move_gripper("near the target location")
```