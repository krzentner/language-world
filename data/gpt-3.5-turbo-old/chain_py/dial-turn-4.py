# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial
    # First, move the gripper roughly around the dial. It doesn't need to be
    # perfectly aligned yet.
    if check("the robot's gripper is not around the dial"):
        robot.put("gripper around dial")
    # Once the gripper is around the dial, start turning it.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial")