
    # Steps:
    #  1. Put gripper near the dial
    #  2. Turn the dial until the door unlocks
    # If the gripper isn't near the dial,
    if check("the gripper is not near the dial"):
        robot.move("gripper near dial")
    # If the gripper is near the dial, just turn it
    # until the door unlocks.
    if check("The gripper is near the dial"):
        robot.turn("dial until door unlocks")