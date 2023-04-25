
    # Steps:
    #  1. Put gripper above the dial
    #  2. Rotate the dial with the gripper
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # Once the gripper is lined up with the dial, rotate the dial with the
    # gripper.
    if check("the robot's gripper is vertically aligned with the dial and the dial is not in the correct position"):
        robot.move_gripper("around the dial")