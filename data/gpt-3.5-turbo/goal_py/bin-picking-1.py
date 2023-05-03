# Steps:
    #  1. Use camera to detect cube and determine its location
    #  2. Move gripper above cube
    #  3. Drop gripper around cube
    #  4. Close gripper around cube
    #  5. Move gripper to target bin
    #  6. Release gripper to drop cube in bin
    # First, use the robot's camera to locate the cube and determine where it is.
    cube_location = robot.get_cube_location()
    # If we can't find the cube, we can't do anything.
    if cube_location is None:
        print("Cube not found, cannot pick and place.")
    # Otherwise, move the gripper above the cube.
    else:
        # Move gripper above cube location
        if check("the robot's gripper is not above cube"):
            robot.move_gripper("above the cube")
        # Move gripper around cube and close gripper around cube
        if check("the robot's gripper is above cube and the robot's gripper is open"):
            robot.move_gripper("near the cube", close_gripper=True)
        # Move gripper to target bin and release gripper to drop cube in bin
        if check("the robot's gripper is above bin"):
            robot.move_gripper("above the target bin")
            robot.move_gripper("near the target bin", close_gripper=False)