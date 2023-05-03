# basketball: put the ball into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Line up the gripper with the hoop
    #  4. Raise the gripper to the height of the hoop
    #  5. Move gripper forward to shoot the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the gripper is around the ball, line up the gripper with the hoop.
    if check("the robot's gripper is around the ball"):
        robot.move_gripper("vertically aligned with the hoop")
    # After the gripper is lined up with the hoop, raise the gripper to the height of the hoop.
    if check("the robot's gripper is vertically aligned with the hoop and the robot's gripper is not at the height of the hoop"):
        robot.move_gripper("at the height of the hoop")
    # Finally, move the gripper forward to shoot the ball into the hoop.
    if check("the robot's gripper is at the height of the hoop and the robot's gripper is not near the hoop"):
        robot.move_gripper("near the hoop")