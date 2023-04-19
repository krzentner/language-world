

The program would look something like this:

```
# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to target location
    # Put the gripper above the cube. We don't have to worry about being too
    # precise here, since we're just trying to grab the cube.
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, move it around the cube to pick it
    # up.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the gripper is around the cube and open, close the gripper to hold the
    # cube.
    if check("the robot's gripper is around the cube and the robot's gripper is closed"):
        robot.move_gripper("towards the target location")
    # If the gripper is holding the cube, move it towards the target location.
    if check("the robot's gripper is holding the cube"):
        robot.move_gripper("above the target location")
```