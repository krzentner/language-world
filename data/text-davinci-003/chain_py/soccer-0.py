
    # Steps:
    #  1. Put gripper near the soccer ball
    #  2. Push soccer ball towards target
    # If the ball is not near the robot's gripper, move the gripper near the
    # ball.
    if check("the robot's gripper is not near soccer ball"):
        robot.move("gripper near soccer ball")
    # If the gripper is near the ball, start pushing it towards the target.
    if check("the robot's gripper is near soccer ball"):
        robot.push("soccer ball to target")