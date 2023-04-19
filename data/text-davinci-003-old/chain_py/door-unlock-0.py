
    # Steps:
    #  1. Put gripper near the knob
    #  2. Line gripper up with the dial
    #  3. Turn the dial
    # First, move the gripper near the knob.
    if check("the robot's gripper is not near the knob"):
        robot.put("gripper near knob")
    # If the robot's gripper is near the knob and the dial isn't lined up with
    # the gripper, line the dial up with the gripper.
    if check("the robot's gripper is near the knob and the knob is not horizontally aligned with the robot's gripper"):
        robot.align("gripper with dial")
    # Now that the dial is lined up, just turn it.
    if check("the knob is horizontally aligned with the robot's gripper"):
        robot.turn("knob")