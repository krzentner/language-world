
    # Steps:
    #  1. Put gripper above the ball
    #  2. Push the ball towards the goal
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    # Once the gripper is above the ball, try to push it towards the goal.
    if check("the robot's gripper is above the ball"):
        robot.push("ball towards goal")