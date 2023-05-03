# Steps:
    #  1. Put gripper above dial
    #  2. Put gripper around dial
    #  3. Turn the dial
    # First, put the gripper roughly above the dial.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the gripper isn't around the dial, move it around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, we can turn it.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("to turn the dial")