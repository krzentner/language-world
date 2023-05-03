
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial
    #  3. Turn dial
    # First, put the robot's gripper above the dial so that it can be lined up
    # and grabbed.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the gripper is lined up with the dial from the side but not around it,
    # move it around the dial.
    if check("the robot's gripper is not around dial and the robot's gripper is almost vertically aligned with dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, turn it to unlock the door.
    if check("the robot's gripper is around dial"):
        robot.move_gripper("right of the dial")