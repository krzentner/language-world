# Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into top of soccer ball
    #  3. Push soccer ball to goal
    # Like with the puck, the robot can slide the soccer ball by trapping it by
    # pushing down on it from above and moving the gripper.
    # If the soccer ball isn't below the gripper as seen from above, move the
    # gripper above the soccer ball.
    if check("the robot's gripper is not above soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper is above the soccer ball, and not near it, move the gripper
    # down to the soccer ball to slide it.
    if check("the robot's gripper is above the soccer ball and the robot's gripper is not near soccer ball"):
        robot.move_gripper("almost vertically aligned with the soccer ball", close_gripper=True)
    # If the gripper is near the soccer ball, we've probably trapped the soccer
    # ball and can slide it to the target location.
    # Close the gripper to make sure we keep control of the soccer ball.
    if check("the robot's gripper is near the soccer ball"):
        robot.move_gripper("above the target location")