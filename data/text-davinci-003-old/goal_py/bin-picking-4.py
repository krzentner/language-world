
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Grasp the cube
    #  4. Place cube in the target bin
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grasp it by
    # closing the gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.move_gripper("above the target bin")
    # Once we've picked up the cube, move it to the bin and drop it in.
    if check("the gripper is near the target bin"):
        robot.move_gripper("above the target bin", close_gripper=False)