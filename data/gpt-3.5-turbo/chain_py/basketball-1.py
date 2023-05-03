# Steps:
    #  1. Put gripper above ball
    #  2. Grab the ball
    #  3. Position the ball above the hoop
    #  4. Drop the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    # If the ball is not in the gripper, we should grab it.
    if check("the ball is not in the gripper and the gripper is open"):
        robot.grab("ball")
    # Position the ball above the hoop, making sure it is centered.
    if check("the ball is in the gripper and the ball is not centered above the hoop"):
        robot.move("ball to center of hoop")
    # Drop the ball into the hoop.
    if check("the ball is centered above the hoop"):
        robot.drop("ball into hoop")