# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the correct combination
    # First, move the gripper around the dial
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Once the gripper is around the dial, turn the dial to the correct
    # combination.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("at the correct combination")