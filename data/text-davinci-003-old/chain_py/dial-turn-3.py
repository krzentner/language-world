
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial handle with the gripper
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # If the gripper isn't near the dial handle, move it near the dial handle.
    if check("the robot's gripper is not near dial handle"):
        robot.grab("dial handle")
    # As long as the gripper is near the dial handle, turn the dial.
    if check("the robot's gripper is near the dial handle"):
        robot.turn("dial")