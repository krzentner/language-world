# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the correct combination
    # To turn the dial, we need to grip it first.
    # If the gripper is not around the dial, move it there.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Use the gripper to turn the dial to the correct combination.
    if check("the robot's gripper is around the dial and the dial is not set to the correct combination"):
        robot.move_gripper("around the dial to the correct combination")