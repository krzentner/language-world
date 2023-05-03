
    # Steps:
    #  1. Put gripper in front of lever
    #  2. Rotate lever up
    # First, put the gripper near the lever.
    if check("the robot's gripper is not forward aligned with lever"):
        robot.move_gripper("forward aligned with the lever")
    # If the gripper is lined up with the lever, we can rotate it up.
    if check("the robot's gripper is forward aligned with the lever"):
        robot.move_gripper("forward aligned with the lever", close_gripper=True)