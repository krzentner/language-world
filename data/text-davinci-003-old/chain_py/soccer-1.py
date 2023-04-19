
    # Steps:
    #  1. Put gripper above the soccer ball
    #  2. Push the soccer ball to the target location
    # First, put the gripper above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.place("gripper above soccer ball")
    # If the gripper is in front of the soccer ball, we can push it.
    if check("the robot's gripper is forward aligned with soccer ball"):
        robot.push("soccer ball to goal")