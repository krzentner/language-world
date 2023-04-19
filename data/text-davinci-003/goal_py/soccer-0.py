
    # Steps:
    #  1. Put gripper below soccer ball
    #  2. Push soccer ball
    # First, put the gripper below the soccer ball, so that we don't bump it
    # while trying to push it.
    if check("the robot's gripper is not below soccer ball"):
        robot.move_gripper("below the soccer ball")
    # Once the gripper is below the soccer ball, we can just push it to the
    # target location.
    if check("the robot's gripper is below soccer ball"):
        robot.move_gripper("horizontally aligned with the target location")