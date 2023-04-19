
    # Steps:
    #  1. Put gripper in front of the lever
    #  2. Grab the lever
    #  3. Pull lever up
    # First, line up the gripper with the lever from the front.
    if check("the robot's gripper is not forward aligned with the lever"):
        robot.move_gripper("forward aligned with the lever")
    # If the gripper isn't around the lever, line it up around the lever.
    if check("the robot's gripper is not around lever"):
        robot.move_gripper("around the lever", close_gripper=True)
    # If the gripper is around the lever, just pull it up.
    if check("the robot's gripper is around lever"):
        robot.move_gripper("upward")