

Then let's fill in the steps:

```
# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Move mug to goal
    # First, put the gripper roughly above mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # If the gripper is near the mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
```