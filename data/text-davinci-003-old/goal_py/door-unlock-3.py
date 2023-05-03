
    # Steps:
    #  1. Put gripper beside the dial
    #  2. Turn the dial
    # If the gripper isn't aligned with the dial, line it up near the dial.
    if check("the robot's gripper is not beside of the dial"):
        robot.move_gripper("beside the dial")
    # If the gripper is aligned with the dial, move it to the right to turn it
    # until the door unlocks.
    if check("the robot's gripper is beside of the dial"):
        robot.move_gripper("right until the door unlocks")