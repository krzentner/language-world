
    # Steps:
    #  1. Put gripper above dial
    #  2. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # Now that the gripper is lined up above the dial, we can turn it.
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.turn("dial")