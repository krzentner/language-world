# Steps:
    #  1. Find the cube using the robot's camera
    #  2. Move the gripper above the center of the cube
    #  3. Drop the gripper around the cube
    #  4. Close the gripper around the cube
    #  5. Move the gripper to the target bin
    #  6. Drop the cube into the target bin
    # Use the robot's vision system to locate the cube in the workspace
    if check("robot does not see the cube"):
        robot.move_camera("near the cube")
    # Move the gripper vertically above the center of the cube
    if check("the robot's gripper is not vertically aligned with the center of the cube"):
        robot.move_gripper("vertically aligned with the center of the cube")
    # Move the gripper down around the cube to pick it up
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the center of the cube", close_gripper=True)
    # Move the gripper to the target bin
    if check("the robot's gripper is not near the target bin"):
        robot.move_gripper("near the target bin")
    # Open the gripper to drop the cube into the target bin
    if check("the robot's gripper is near the target bin and the robot's gripper is closed"):
        robot.move_gripper("above the target bin", close_gripper=False)