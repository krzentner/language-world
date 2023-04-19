
    # Steps:
    #  1. Put gripper in front of the lock
    #  2. Turn the dial of the lock
    # Put the gripper in front of the lock. Align the gripper from the top
    # because of the angle of the dial, to make sure it's lined up.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial", close_gripper=True)
    # Once the robot's gripper is lined up, simply turn the dial.
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.move_gripper("around the dial")