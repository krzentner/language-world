
    # Steps:
    #  1. Put gripper just above soccer ball
    #  2. Push soccer ball towards goal
    # First, put the gripper slightly above the soccer ball.
    # We don't want the robot's gripper to bang the soccer ball away, because
    # that would be sloppy.
    if check("the robot's gripper is not slightly above soccer ball"):
        robot.put("gripper slightly above soccer ball")
    # If the gripper is above the soccer ball, we can start pushing the ball
    # towards the goal.
    # Push it in the direction of the goal.
    if check("the robot's gripper is looking down at soccer ball and the robot's gripper is not near the goal"):
        robot.push("soccer ball towards goal")