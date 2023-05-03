# Steps:
    #  1. Approach the soccer ball
    #  2. Put gripper around soccer ball
    #  3. Push soccer ball towards the goal
    # Approach the soccer ball by moving the robot's gripper towards it.
    if check("the robot's gripper is not near the soccer ball"):
        robot.approach("soccer ball")
    # Once the gripper is near the soccer ball, put it around the ball.
    if check("the robot's gripper is near the soccer ball and the robot's gripper is not around the soccer ball"):
        robot.drop("gripper around soccer ball")
    # If the gripper is around the soccer ball, start pushing it towards the
    # goal by sliding it.
    # We can keep the gripper closed to keep control of the ball.
    if check("the robot's gripper is around the soccer ball and the soccer ball is in front of the robot's gripper"):
        robot.slide("the soccer ball towards the goal")