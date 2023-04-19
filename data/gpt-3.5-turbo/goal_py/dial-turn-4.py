# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial

    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.move_gripper("near the dial", close_gripper=True)

    # Once the gripper is around the dial, we can turn it.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("turn the dial")