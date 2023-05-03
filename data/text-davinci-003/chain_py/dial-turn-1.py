
    # Steps:
    #  1. Put gripper align with dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial
    # The dial is a small object that we need to carefully align the gripper
    # with in order to securely grab it with its two small fingers.
    # First, line up the robot's gripper with the dial so it can try to grab it.
    if check("the robot's gripper is not horizontally linke up with the dial and the robot's gripper is not vertically aligned with the dial"):
        robot.align("gripper with dial")
    # If the gripper is still mostly in front of the dial, we can move the two
    # gripper fingers around the dial.
    # If the gripper is already around the dial, close the gripper around the
    # dial.
    if check("the robot's gripper is horizontally linked up with the dial and the robot's gripper is not around dial"):
        robot.grab("dial")
    # If the gripper is already around the dial, close the gripper around the
    # dial.
    if check("the robot's gripper is around dial"):
        robot.close("gripper around dial")
    # Finally, we can rotate the dial.
    if check("the robot's gripper is closed around dial and the robot is lined up with the target direction of the dial"):
        robot.rotate("dial to target direction")