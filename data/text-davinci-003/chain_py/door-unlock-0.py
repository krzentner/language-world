
    # Steps:
    #  1. Put gripper above dial
    #  2. Close gripper around dial
    #  3. Turn clockwise until the door is unlocked
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertical aligned with the dial"):
        robot.put("gripper above dial")
    # If the gripper isn't near the dial, move the gripper to the dial.
    if check("the robot's gripper is not near the dial"):
        robot.put("gripper around dial")
    # When the gripper is closed around the dial, turn the dial clockwise until
    # the door is unlocked.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial clockwise until unlocked")