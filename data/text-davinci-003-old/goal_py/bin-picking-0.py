
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to target bin
    # First, move the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above the cube")
    # Then, drop the gripper down around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, try to grab it by closing the
    # gripper.
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.move_gripper("above the target bin")
    # Once the gripper has the cube, move it to the target bin.
    if check("the robot's gripper is above the target bin"):
        robot.move_gripper("near the target bin")