# Steps:
    #  1. Align gripper above ball
    #  2. Grab ball with gripper
    #  3. Align gripper and ball with hoop
    #  4. Push ball towards hoop
    #  5. Release ball into hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not aligned with the ball"):
        robot.move_gripper("above the ball")
    # If the gripper is above the ball, we can probably grab it.
    if check("the robot's gripper is above the ball and the robot's gripper is not holding the ball"):
        robot.move_gripper("around the ball", close_gripper=True)
    # If the ball is in the gripper and the gripper is not aligned with the hoop,
    # align the gripper and ball with the hoop.
    if check("the robot's gripper is holding the ball and the robot's gripper is not aligned with the hoop"):
        robot.move_gripper("aligned with the hoop")
    # If the gripper and ball are aligned with the hoop, push the ball towards the
    # hoop.
    if check("the robot's gripper is aligned with the hoop and the ball is in front of the hoop"):
        robot.move_gripper("inside the hoop", close_gripper=False)