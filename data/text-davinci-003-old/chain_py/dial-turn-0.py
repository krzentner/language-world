
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial
    # Put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # If the dial becomes left of the gripper, go back to putting the gripper
    # above the dial.
    # Because the dial is a thin object, check if the gripper is lined up with it
    # from the side instead of around it.
    if check("dial is not left of the robot's gripper and dial is not side aligned with the robot's gripper"):
        robot.grab("dial")
    # Now that the dial is in the gripper, turn the dial.
    if check("the robot's gripper is side aligned with the dial"):
        robot.turn("dial")