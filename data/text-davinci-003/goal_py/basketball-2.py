
    # Steps:
    #  1. Put gripper above ball
    #  2. Drop Gripper around ball
    #  3. Elevate Gripper slightly
    #  4. Push ball towards hoop
    #  5. Release ball under rim
    # First, put the gripper roughly above ball, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above ball"):
        robot.move_gripper("above ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.move_gripper("around ball", close_gripper=True)
    # If the gripper is near the ball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above ball and the gripper is closed"):
        robot.move_gripper_elev(slightly_above_reference_surface)
    # If the gripper is slightly elevated, we can push the ball towards the hoop.
    if check("the robot's gripper is slightly elevated above the reference surface"):
        robot.move_gripper("towards the hoop")
    # If the ball is near the hoop, we can aim it at the hoop and then release it.
    if check("the ball is near the hoop"):
        robot.move_gripper("left of the hoop")