    # Steps:
    #  1. Put gripper around dial
    #  2. Turn dial to the desired position
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Once the gripper is around the dial, we can turn it to the desired
    # position.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("in the desired position")