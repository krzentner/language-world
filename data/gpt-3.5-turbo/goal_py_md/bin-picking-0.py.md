# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Position the gripper above the cube in the bin
    #  2. Close the gripper around the cube
    #  3. Lift the gripper out of the bin
    #  4. Position the gripper over the target bin
    #  5. Move the gripper down towards the target bin
    #  6. Release the cube into the target bin
    # First, position the gripper above the cube in the bin.
    if check("the robot's gripper is not above the cube in the bin"):
        robot.move_gripper("above the cube in the bin")
    # Close the gripper around the cube.
    if check("the robot's gripper is above the cube in the bin and the robot's gripper is open"):
        robot.move_gripper("around the cube in the bin", close_gripper=True)
    # Lift the gripper out of the bin.
    if check("the robot's gripper is around the cube in the bin and the robot's gripper is not above the bin"):
        robot.move_gripper("above the bin")
    # Position the gripper over the target bin.
    if check("the robot's gripper is not above the target bin"):
        robot.move_gripper("above the target bin")
    # Move the gripper down towards the target bin.
    if check("the robot's gripper is above the target bin and the robot's gripper is not near the bin"):
        robot.move_gripper("near the bin")
    # Release the cube into the target bin.
    if check("the robot's gripper is near the bin and closed"):
        robot.move_gripper("open", close_gripper=False)