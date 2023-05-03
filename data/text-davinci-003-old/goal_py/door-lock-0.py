
    # Steps:
    #  1. Put the gripper above the dial
    #  2. Put the gripper around the dial
    #  3. Turn the dial clockwise
    # The door lock has a dial, so we need to line up the robot's gripper as
    # seen from above to rotate it.
    if check("robot's gripper is not vertically aligned with dial"):
        robot.move_gripper("vertically aligned with the dial",close_gripper=True)
    # If the gripper is lined up from above, move the gripper down to the dial
    # and rotate the dial clockwise.
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not near dial"):
        robot.move_gripper("around the dial")
    # If the gripper is near the dial, rotate the dial clockwise until the
    # door is unlocked.
    if check("the robot's gripper is near dial"):
        robot.turn_dial("clockwise")