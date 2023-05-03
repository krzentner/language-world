# Steps:
    # 1. Put gripper above soccer ball
    # 2. Push gripper into top half of soccer ball
    # 3. Push soccer ball to goal
    # The robot can push the soccer ball in a similar way to pushing the puck.
    # If the soccer ball isn't below the gripper as seen from above, move the
    # gripper above the ball.
    if check("the robot's gripper is not above soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper is aligned with the ball but not near it, move the gripper
    # down to the ball to slide it.
    if check("the robot's gripper is not below soccer ball and the robot's gripper is vertically aligned with the soccer ball"):
        robot.move_gripper("below the soccer ball")
    # If the gripper is near the ball, we've probably trapped the ball and can
    # push it to the target location.
    # Close the gripper to make sure we keep control of the ball.
    if check("the robot's gripper is near the soccer ball"):
        robot.move_gripper("above the target location")