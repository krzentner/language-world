```
# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Move gripper above the cube
    #  2. Grab cube with gripper
    #  3. Move gripper above target bin
    #  4. Drop cube into bin
    # First, move the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube and closed, move it above the target
    # bin.
    if check("the robot's gripper is around the cube and the robot's gripper is closed"):
        robot.move_gripper("above the target bin")
    # Drop the cube into the target bin.
    if check("the robot's gripper is above the target bin"):
        robot.move_gripper("near the bottom of the target bin", open_gripper=True)
```