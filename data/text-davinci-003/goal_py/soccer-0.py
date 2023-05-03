
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into soccer ball
    #  3. Push soccer ball to goal
    # First, the robot should move the gripper above the soccer ball
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper isn't near the soccer ball, move the gripper to the soccer
    # ball to push it.
    if check("the robot's gripper is not near the soccer ball"):
        robot.move_gripper("above the soccer ball", close_gripper=True)
    # If the gripper is near the soccer ball, we've probably trapped it and can
    # push it to the target location.
    if check("the robot's gripper is near the soccer ball and the soccer ball is below the robot's gripper"):
        robot.move_gripper("above the target location")