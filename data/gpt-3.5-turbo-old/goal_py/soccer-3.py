# Steps:
    #  1. Put gripper above the soccer ball
    #  2. Grab the soccer ball with the gripper
    #  3. Push the soccer ball into the goal
    # First, put the gripper above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper is above the soccer ball, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above the soccer ball and the robot's gripper is open"):
        robot.move_gripper("near the soccer ball", close_gripper=True)
    # If the gripper is near the soccer ball, we've probably trapped it and can 
    # push it to the goal.
    # Close the gripper to make sure we keep control of the ball.
    if check("the robot's gripper is near the soccer ball"):
        robot.move_gripper("above the target location")