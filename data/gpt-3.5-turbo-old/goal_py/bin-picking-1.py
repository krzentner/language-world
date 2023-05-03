# Steps:
    #  1. Move the gripper above the cube
    #  2. Close the gripper around the cube
    #  3. Lift the cube off the table
    #  4. Move the gripper above the target bin
    #  5. Lower the cube into the bin
    #  6. Open the gripper to release the cube
    # First, put the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Once the gripper is around the cube, lift it off the table.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("in the air")
    # Move the gripper above the target bin.
    if check("the robot's gripper is not above the target bin"):
        robot.move_gripper("above the target bin")
    # Lower the cube into the bin.
    if check("the robot's gripper is above the target bin"):
        robot.move_gripper("in the bin", open_gripper=True)