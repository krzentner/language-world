
    # Steps:
    #  1. Put robot near soccer ball
    #  2. Push soccer ball towards goal
    #  3. Kick soccer ball towards goal
    # First, move the robot near the soccer ball.
    if check("the robot's feet are not near soccer ball"):
        robot.move("feet near soccer ball")
    # If the robot is near the soccer ball, we can start pushing it.
    if check("the robot's feet are near the soccer ball"):
        robot.push("soccer ball towards goal")
    # If the soccer ball is close to the goal, attacking it by kicking at it.
    if check("the soccer ball is close enough to the goal for the robot to kick it"):
        robot.kick("soccer ball towards goal")