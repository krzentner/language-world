# Steps:
    #  1. Put gripper around the knob of the dial
    #  2. Turn dial clockwise or counterclockwise based on the target
    # First, put the gripper around the knob of the dial.
    if check("the robot's gripper is not around the dial knob"):
        robot.drop("gripper around dial knob")
    # If the dial is supposed to be turned clockwise, turn it clockwise.
    # Otherwise, turn it counterclockwise.
    if check("the robot's gripper is around the dial knob"):
        if target == "clockwise":
            robot.push("dial clockwise")
        else:
            robot.push("dial counterclockwise")