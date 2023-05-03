# Steps:
    #  1. Put gripper above soccer ball
    #  2. Drop gripper around soccer ball
    #  3. Push soccer ball to goal
    # First, put the gripper roughly above the soccer ball, so that we don't bump
    # it while trying to grab it.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper isn't around the soccer ball, put it around the soccer ball.
    if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.move_gripper("near the soccer ball", close_gripper=True)
    # If the gripper is near the soccer ball, we've probably trapped the soccer
    # ball and can push it towards the goal.
    # Close the gripper to make sure we keep control of the soccer ball.
    if check("the robot's gripper is near the soccer ball and the soccer ball is below the robot's gripper"):
        robot.move_gripper("above the target location")