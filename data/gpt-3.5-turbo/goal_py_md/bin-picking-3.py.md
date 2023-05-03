# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Close gripper around the cube
    #  4. Move the cube to the target bin
    if check("the robot's gripper is not positioned over the cube"):
        robot.move_gripper("over the cube")
    if check("the robot's gripper is not positioned around the cube"):
        robot.move_gripper("around the cube")
    if check("the robot's gripper is positioned around the cube and is open"):
        robot.move_gripper("closed around the cube")
    if check("the robot's gripper is not positioned over the target bin"):
        robot.move_gripper("over the target bin")
    if check("the robot's gripper is positioned over the target bin and the gripper is closed"):
        robot.move_gripper("above the target bin")