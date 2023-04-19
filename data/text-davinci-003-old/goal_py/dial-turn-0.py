
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the gripper isn't around the dial, put it around the dial.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Once the gripper is around the dial, we can turn it.
    if check("the robot's gripper is around dial"):
        robot.move_gripper("near the dial")