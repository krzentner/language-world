# Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Move the gripper above the hoop
    #  4. Release the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move("gripper to above the ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.grab("the ball")
    # Once the ball is in the gripper, we can move it above the hoop.
    if check("the robot's gripper has the ball and the gripper is not above the hoop"):
        robot.move("gripper to above the hoop")
    # Drop the ball into the hoop.
    if check("the robot's gripper is above the hoop"):
        robot.release("the ball into the hoop")