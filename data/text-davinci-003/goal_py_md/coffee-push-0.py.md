

Then, write the commands to perform the task:

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Push the mug to the target location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.move_gripper("vertically aligned with the mug handle")
    # Now that the gripper is lined up above the mug handle, we should be able to
    # grab the mug handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Once the mug is in the gripper, we can just push the mug to the target location.
    if check("the robot's gripper is around mug handle"):
        robot.move_gripper("above the target location")
```