# Steps:
    #  1. Use camera to locate cube
    #  2. Position gripper above cube in a way that allows for a good grip
    #  3. Close gripper around cube
    #  4. Lift cube and move it to target bin
    # Use the robot's camera to locate the cube in the workspace.
    if check("the robot's camera cannot see the cube"):
        robot.move_camera("to view the cube")
    # Position the gripper above the cube in a way that allows for a good grip.
    if check("the gripper is not properly positioned and ready to pick up the cube"):
        robot.move_gripper("above the cube", close_gripper=False)
    # Close the gripper around the cube to pick it up.
    if check("the cube is not held securely by the gripper"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Lift the cube and move it to the target bin.
    if check("the gripper is not positioned over the target bin"):
        robot.move_gripper("over the target bin", close_gripper=True)
    if check("the cube has not been released into the target bin"):
        robot.move_gripper("above the target bin", close_gripper=False)