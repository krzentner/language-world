
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push soccer ball forwards
    #  3. Move soccer ball to goal
    # The robot can indirectly push the soccer ball by holding it from the top and
    # pushing forward.
    # First, put the gripper above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper is above the soccer ball but not in contact with it, we can
    # move the gripper in contact with it to start pushing.
    if check("the robot's gripper is above the soccer ball and the robot's gripper is not near the soccer ball"):
        robot.move_gripper("near the soccer ball", close_gripper=True)
    # If the gripper is in contact with the soccer ball, we can start pushing it.
    if check("the robot's gripper is near the soccer ball and the robot's gripper is closed"):
        robot.move_gripper("forward aligned with the soccer ball")
    # Once we've pushed the soccer ball far enough, move it to the goal.
    if check("the robot's gripper is forward aligned with soccer ball"):
        robot.move_gripper("above the target location")