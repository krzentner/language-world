# Steps:
    #  1. Move towards the soccer ball
    #  2. Position the robot's gripper behind the soccer ball
    #  3. Push the soccer ball towards the goal
    # First, move the robot towards the soccer ball.
    if check("the robot is not positioned near the soccer ball"):
        robot.move("towards the soccer ball")
    # Once the robot is near the soccer ball, position the gripper behind it.
    if check("the robot is positioned near the soccer ball and the robot's gripper is not behind the soccer ball"):
        robot.put("the gripper behind the soccer ball")
    # When the gripper is behind the soccer ball, push the ball towards the
    # goal.
    if check("the robot's gripper is behind the soccer ball"):
        robot.push("the soccer ball towards the goal")