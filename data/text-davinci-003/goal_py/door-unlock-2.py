
    # Steps:
    #  1. Put gripper above dial
    #  2. Drop gripper around dial, then rotate it
    # If the gripper isn't above the dial, move it above the dial.
    if check("the robot's gripper is not above the dial and the robot's gripper is not almost vertically aligned with the dial"):
        robot.move_gripper("almost vertically aligned with the dial", close_gripper=True)
    # If the gripper is almost lined up, closing it should fully line it up.
    if check("the robot's gripper is almost vertically aligned with the dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, just rotate it!
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("around the dial", rotations=1)