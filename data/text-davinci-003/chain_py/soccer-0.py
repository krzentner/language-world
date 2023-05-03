
    # Steps:
    #  1. Put gripper above ball
    #  2. Push gripper into top of ball
    #  3. Slide ball to goal
    # The robot can slide the ball by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the ball isn't below the gripper as seen from above, move the gripper
    # above the ball.
    if check("the robot's gripper is not above ball and the robot's gripper is not vertically aligned with the ball"):
        robot.put("the gripper above the ball")
    # If the gripper is aligned with the ball but not near it, move the gripper
    # down to the ball to slide it.
    if check("the robot's gripper is vertically aligned with the ball and the robot's gripper is not near ball"):
        robot.push("the gripper into the ball")
    # If the gripper is near the ball, we've probably trapped the ball and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the ball.
    if check("the robot's gripper is near the ball and the ball is below the robot's gripper"):
        robot.slide("the ball to the goal")