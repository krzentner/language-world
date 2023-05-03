


# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Close gripper around cube
    #  3. Move cube to target bin
    # First, put the gripper above the cube. 
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't closed around the cube, move it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("below the cube", close_gripper=True)
    # If the gripper is near the cube and closed, move the cube to the target
    # bin.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("above the target bin")