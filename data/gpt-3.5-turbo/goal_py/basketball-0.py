# Steps:
    # 1. Move the gripper over the ball
    # 2. Grip the ball
    # 3. Move the ball towards the hoop
    # 4. Release the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # If the gripper is above the ball, close the gripper to grip the ball.
    if check("the robot's gripper is vertically aligned with the ball and the robot's gripper is not around the ball"):
        robot.move_gripper("around the ball")
    # Move the ball towards the hoop.
    if check("the robot's gripper is around the ball and the robot's gripper is not near the hoop"):
        robot.move_gripper("near the hoop")
    # Finally, release the ball into the hoop.
    if check("the robot's gripper is near the hoop and the robot's gripper is around the ball"):
        robot.move_gripper("above the ball", close_gripper=False)