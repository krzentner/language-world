
    # Steps:
    #  1. Put gripper above the dial
    #  2. Turn the dial
    # First, we need to get the gripper above the dial handle.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # Once the gripper is lined up with the handle, move it to the left or right
    # to start turning the dial.
    if check("the robot's gripper is not horizontally aligned with the dial"):
        robot.move_gripper("above the dial handle")