# Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Move the gripper above the hoop
    #  4. Drop the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # If the gripper is near the ball and open, close the gripper to hold the ball.
    if check("the robot's gripper is near the ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # Move the gripper above the hoop.
    if check("the robot's gripper is holding the ball and is not above the hoop"):
        robot.move("gripper above hoop")
    # Drop the ball into the hoop.
    if check("the robot's gripper is holding the ball and is above the hoop"):
        robot.drop("ball into hoop")