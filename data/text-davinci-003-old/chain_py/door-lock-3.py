
    # Steps:
    #  1. Put gripper above the dial
    #  2. Line up the gripper with the dial
    #  3. Turn the dial
    # First, the robot should align the gripper with the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # Once the gripper is roughly lined up with the dial, turn the dial.
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.turn("the dial")