# Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn dial to the correct combination
    # First, put the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # If the gripper isn't around the dial, put it around the dial.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.move_gripper("near the dial", close_gripper=True)
    # Now, we can turn the dial to the correct combination.
    robot.turn_dial("correct combination")