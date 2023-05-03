
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Sweep cube to goal
    # First, put the gripper above the cube. This isn't necessary, but it will
    # help line up the robot's gripper with the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Once the gripper is closed around the cube, we can sweep the cube to the
    # target location.
    if check("the robot's gripper is around the cube and the robot's gripper is closed"):
        robot.move_gripper("right of the target location")