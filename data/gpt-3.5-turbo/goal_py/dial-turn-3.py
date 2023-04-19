# Steps:
    #  1. Put the gripper above the dial
    #  2. Place the gripper on the dial
    #  3. Rotate the gripper to turn the dial
    # First, put the gripper roughly above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # If the gripper is above the dial but not gripping it, move the gripper
    # down onto the dial.
    if check("the robot's gripper is above the dial and the robot's gripper is not gripping the dial"):
        robot.move_gripper("on the dial", close_gripper=True)
    # Now that the gripper is gripping the dial, we can rotate it to turn the
    # dial.
    if check("the robot's gripper is gripping the dial and the dial is not turned to the desired position"):
        robot.move_gripper("near the desired position")