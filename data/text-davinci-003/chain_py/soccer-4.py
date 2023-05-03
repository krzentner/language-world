
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Drop gripper around soccer ball
    #  3. Push soccer ball to goal
    # First, put the gripper above the soccer ball
    if check("the robot's gripper is not above the soccer ball"):
        robot.place("gripper above soccer ball")
    # If the gripper isn't around the soccer ball, put it around the soccer ball.
    if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.drop("gripper around soccer ball")
    # Now that the gripper is around the soccer ball, we can slide it to the
    # goal by pushing against the ball
    if check("the robot's gripper is around the soccer ball"):
        robot.push("soccer ball to goal")