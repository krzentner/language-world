# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Move gripper above the cube.
    #  2. Position gripper around the cube.
    #  3. Close gripper around the cube.
    #  4. Move gripper to target bin.
    #  5. Open gripper to release the cube into the bin.
    
    # Move the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    
    # Position gripper around the cube.
    if check("the robot's gripper is not around the cube"):
        robot.move_gripper("near the cube")
    
    # Close gripper around the cube.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    
    # Move gripper to target bin.
    if check("the robot's gripper is holding the cube and is not near the target bin"):
        robot.move_gripper("near the target bin")
    
    # Open gripper to release the cube into the bin.
    if check("the robot's gripper is near the target bin and is holding the cube"):
        robot.move_gripper("near the target bin", open_gripper=True)