# Steps:
    #  1. Put the gripper on the dial
    #  2. Close the gripper around the dial
    #  3. Turn the dial to the desired position
    # Align the gripper with the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # Close the gripper to grab the dial.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Turn the dial to the desired position.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("at the desired dial position")