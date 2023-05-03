
    # Steps:
    #  1. Put gripper in front of soccer ball
    #  2. Push soccer ball to goal
    # If the soccer ball is not within reach of the robot's gripper, move the 
    # gripper in front of the soccer ball.
    if check("the soccer ball is not near robot's gripper"):
        robot.put("gripper in front of soccer ball")
    # If the robot's gripper is near the soccer ball, we can push it to the goal.
    if check("the robot's gripper is near the soccer ball"):
        robot.push("soccer ball to goal")