# Steps:
    #  1. Use camera to determine location of cube
    #  2. Move gripper above cube
    #  3. Grab cube with gripper
    #  4. Use camera to determine location of target bin
    #  5. Move gripper above target bin
    #  6. Release cube into target bin
    # We can use the camera to determine the location of the cube and target bin.
    # First, move the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper is above the cube but not around it, move it down around the cube.
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube and the robot's gripper is closed"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Once the gripper is around the cube, use the camera to determine the location of the target bin.
    # Move the gripper above the target bin.
    if check("the robot's gripper is around the cube and the robot's gripper is not above the target bin"):
        robot.move_gripper("above the target bin")
    # Release the cube into the target bin.
    if check("the robot's gripper is above the target bin and the robot's gripper is open"):
        robot.move_gripper("away from the target bin")