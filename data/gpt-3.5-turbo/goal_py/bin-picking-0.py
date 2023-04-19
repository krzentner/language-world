# Steps:
    #  1. Scan the area and locate the cube and target bin
    #  2. Calculate the path to the cube, avoiding any obstacles
    #  3. Move the gripper to the cube
    #  4. Close the gripper around the cube
    #  5. Calculate the path to the target bin, avoiding any obstacles
    #  6. Move the gripper to the target bin
    #  7. Release the cube into the bin
    # First, scan the area and locate the cube and target bin.
    cube_location = scan_for_object("cube")
    bin_location = scan_for_object("bin")
    # Next, calculate a path to the cube, avoiding any obstacles.
    path_to_cube = calculate_path(robot.current_location, cube_location)
    # Follow the path to the cube.
    follow_path(robot, path_to_cube)
    # Once we've reached the cube, move the gripper around it and close it.
    if check("the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Next, calculate a path to the target bin, avoiding any obstacles.
    path_to_bin = calculate_path(robot.current_location, bin_location)
    # Follow the path to the bin.
    follow_path(robot, path_to_bin)
    # Once we've reached the target bin, release the cube into the bin.
    if check("the robot's gripper is not above the bin"):
        robot.move_gripper("above the bin")
    if check("the robot's gripper is above the bin and the gripper is closed"):
        robot.move_gripper("open", close_gripper=False)