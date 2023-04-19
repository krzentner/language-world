
    # Steps:
    #  1. Align the gripper with the dial
    #  2. Push the dial slowly in the unlocking direction
    # First, align the gripper with the dial.
    if check("the robot's gripper is not aligned with dial"):
        robot.move_gripper("aligned with dial")
    # With the robot's gripper aligned with the dial, just slowly push the dial
    # in the unlocking direction.
    if check("the robot's gripper is aligned with dial"):
        robot.move_gripper("clockwise")