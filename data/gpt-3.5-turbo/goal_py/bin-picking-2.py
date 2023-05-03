# Steps:
    #  1. Identify and locate the cube
    #  2. Move gripper above the cube
    #  3. Lower gripper to grab the cube
    #  4. Move gripper above target bin
    #  5. Release the cube into the bin
    # First, we need to locate the cube using object recognition.
    if check("cube is not in view of the robot's camera"):
        robot.move_camera("to locate the cube")
    # Once the cube is located, move the gripper above it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # Lower the gripper to grab the cube once it is above it.
    if check("the robot's gripper is above the cube and the robot's gripper is not closed"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Move the gripper above the target bin.
    if check("the robot's gripper is closed and not above target bin"):
        robot.move_gripper("above the target bin")
    # Release the cube into the bin once it is above it.
    if check("the robot's gripper is above the target bin and the robot's gripper is closed"):
        robot.move_gripper("open above the target bin")