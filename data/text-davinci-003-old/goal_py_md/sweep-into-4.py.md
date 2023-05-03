

Then, complete the program:

```
# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Move the gripper in an arc, from above the cube to the target location
    #  2. Close the gripper around the cube
    #  3. Move to the target location with the cube in the gripper
    # First, move the gripper in a sweeping arc, starting above the cube and
    # ending above the target location.
    if check("the robot's gripper is not in an arc, from above the cube to the target location"):
        robot.move_gripper("in an arc, from above the cube to the target location")
    # Once the gripper is above the cube, close it around the cube.
    if check("the robot's gripper is near the cube"):
        robot.move_gripper("above the cube", close_gripper=True)
    # If the gripper is closed around the cube, we can move to the target location.
    if check("the robot's gripper is closed around the cube"):
        robot.move_gripper("above the target location")
```