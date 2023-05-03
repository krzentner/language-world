# Steps:
    #  1. Put gripper around dial
    #  2. Turn dial to desired position
    # First, align the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, turn it to the desired position.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("almost vertically aligned with the desired position")