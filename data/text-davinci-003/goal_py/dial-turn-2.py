
    # Steps:
    #  1. Put gripper above the dial
    #  2. Push gripper against the dial and turn it
    # This is a tricky motion, since the dial is small and the gripper was not
    # designed for this motion.
    # To make sure we don't break the dial, we should be careful about the
    # gripper.
    # First, move the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the gripper is above the dial but not near it, move the gripper near
    # it, but be gentle.
    if check("the robot's gripper is not near the dial and the robot's gripper is not above the dial"):
        robot.move_gripper("almost vertically aligned with the dial", close_gripper=True)
    # Once the gripper is near the dial, push against it to rotate it.
    if check("the robot's gripper is near the dial and the robot's gripper is closed"):
        robot.move_gripper("around the dial")