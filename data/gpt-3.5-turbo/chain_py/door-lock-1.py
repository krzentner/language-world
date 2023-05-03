# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the correct position
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.put("gripper around dial")
    # Now that the gripper is around the dial, turn it to the correct position.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial to correct position")