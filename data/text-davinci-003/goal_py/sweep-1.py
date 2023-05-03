
    # Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Close gripper around the cube
    #  4. Sweep the cube to the side
    # If the gripper isn't above the cube, put it above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper is above the cube but not around it, move it around the
    # cube.
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the gripper is around the cube and closed, sweep it to the side.
    if check("the robot's gripper is closed around the cube"):
        robot.move_gripper("left of the target")