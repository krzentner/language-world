# Steps:
    #  1. Put gripper over the dial
    #  2. Turn the dial to the correct position
    # First, put the gripper over the dial.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper over the dial")
    # Turn the dial to the correct position
    robot.turn("dial to unlock position")