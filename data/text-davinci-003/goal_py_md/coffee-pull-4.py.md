

Then, write the following code:

```
# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug handle
    #  4. Pull the mug to goal
    # We need to put the gripper roughly above the mug handle before we can grab
    # it, because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.move_gripper("vertically aligned with the mug handle")
    # Once the gripper is lined up above the mug handle, we should be able to
    # grab the mug handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with mug handle, and the robot's gripper is not around mug handle"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Once the gripper is around the mug handle, we can just pull the mug to the
    # target location.
    if check("the robot's gripper is around mug handle"):
        robot.move_gripper("near the target location")
```