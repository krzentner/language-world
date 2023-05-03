
    # Steps:
    #  1. Line up the robot's gripper to the dial
    #  2. Turn the dial with the gripper
    # Line up the robot's gripper with the dial.
    # We can do this by using put() command to move the gripper above the dial
    # from the side, and then using tilt() command to line it up from above.
    if check("the robot's gripper is not aligned with the dial"):
        robot.put("the gripper above the dial")
        robot.tilt("the gripper to dial")
    # Now that the gripper is aligned, just turn the dial.
    if check("the robot's gripper is aligned with the dial"):
        robot.turn("the dial with the gripper")