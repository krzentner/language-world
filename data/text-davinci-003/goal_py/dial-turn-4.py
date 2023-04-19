
    # Steps:
    #  1. Place the robot's gripper above the dial handle
    #  2. Grab the dial handle with a gripping motion
    #  3. Turn the dial handle as requested
    # If the dial handle is not left of the robot's gripper, move the gripper
    # near the dial handle.
    if check("the robot's gripper is left of the dial handle and the robot's gripper is not near the dial handle"):
        robot.move_gripper("near the dial handle", close_gripper=True)
    # If the robot's gripper is near the dial handle, start turning the dial
    # handle as requested.
    if check("the robot's gripper is near the dial handle"):
        robot.move_gripper("around the dial handle")