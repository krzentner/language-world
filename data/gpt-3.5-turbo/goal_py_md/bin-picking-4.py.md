# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Move gripper above the cube
    #  2. Lower gripper onto the cube
    #  3. Close gripper to pick up the cube
    #  4. Move the cube to the target bin
    #  5. Release the cube into the bin.
    
    # First, move the gripper above the cube
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
        
    # Lower the gripper onto the cube
    if check("the robot's gripper is not near the cube"):
        robot.move_gripper("near the cube")
        
    # Close gripper to pick up the cube
    if check("the robot's gripper is not closed around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
        
    # Move the cube to the target bin
    if check("the robot's gripper is not near the target bin"):
        robot.move_gripper("near the target bin")
        
    # Release the cube into the bin
    if check("the robot's gripper is not open above the target bin"):
        robot.move_gripper("above the target bin", close_gripper=False)