# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    # 1. Move the gripper above the cube
    # 2. Drop the gripper around the cube and close it
    # 3. Lift the cube
    # 4. Move to the target bin
    # 5. Drop the cube in the target bin
    
    # Move the gripper above the cube
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
        
    # If the gripper isn't around the cube, put it around the cube and close it
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)

    # Lift the cube
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("above the cube")
        
    # Move to the target bin
    if check("the robot's gripper is not near the target bin"):
        robot.move_gripper("near the target bin")
        
    # Drop the cube in the target bin
    if check("the robot's gripper is near the target bin and the robot's gripper is closed"):
        robot.move_gripper("above the target bin", close_gripper=False)