
    # Steps:
    #  1. Line up the robot's gripper with the hoop
    #  2. Shoot the ball
    # First, line up the robot's gripper with the hoop.
    if check("the robot's gripper is not horizontally aligned with the hoop"):
        robot.move_gripper("horizontally aligned with the hoop")
    # Now that the robot's gripper is lined up with the hoop, we can shoot the
    # ball by moving the gripper towards the hoop.
    if check("the robot's gripper is horizontally aligned with the hoop"):
        robot.move_gripper("above the hoop")