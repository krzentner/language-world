# Steps:
    #  1. Put gripper above ball
    #  2. Push gripper into top of ball
    #  3. Move ball to goal
    # The robot can push the soccer ball by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the ball isn't below the gripper as seen from above, move the gripper
    # above the ball.
    if check("the robot's gripper is not above the ball and the ball is not in front of the gripper"):
        robot.put("gripper above ball")
    # If the gripper is aligned with the ball but not near it, move the gripper
    # down to the ball to push it.
    if check("the robot's gripper is vertically aligned with ball and the ball is not below the gripper"):
        robot.push("gripper into ball")
    # If the gripper is near the ball, we've probably trapped the ball and can
    # push it to the goal location.
    if check("the robot's gripper is near the ball and the ball is below the gripper"):
        robot.move("ball to goal")