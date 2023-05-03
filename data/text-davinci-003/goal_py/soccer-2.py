
    # Steps:
    #  1. Put gripper near soccer ball
    #  2. Push soccer ball towards goal
    # First, move the gripper near the soccer ball.
    # We don't need to be careful about the direction because we'll just be
    # pushing in an arc to the target location.
    if check("the robot's gripper is not near soccer ball"):
        robot.move_gripper("near the soccer ball", close_gripper=True)
    # Once the gripper is near it, push the ball with the gripper.
    if check("the robot's gripper is near the soccer ball"):
        robot.move_gripper("near the target location")