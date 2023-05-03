

Then add the code to perform the following steps: 

1. Put gripper above mug.
2. Grab mug with gripper
3. Move mug to target location.

```
# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab mug with gripper
    #  3. Move mug to target location
    # First, put the gripper roughly above mug. We don't want to bump it while
    # grabbing it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.move_gripper("near the mug", close_gripper=True)
    # Then, move the mug to the target location.
    if check("the robot's gripper is near the mug and the mug is below the robot's gripper"):
        robot.move_gripper("near the target location")
```