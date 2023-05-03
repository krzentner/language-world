
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial to the desired position
    # First, put the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above dial")
    # If the gripper isn't around the dial, put it around the dial.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # If the gripper is around the dial, start turning.
    if check("the robot's gripper is around the dial and the robot's gripper is closed"):
        robot.move_gripper("above the desired position")