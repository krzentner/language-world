
    # Steps:
    #  1. Locate the dial
    #  2. Put gripper around dial and close
    #  3. Rotate the dial to the right direction
    # The robot can just move the gripper directly to the dial, since we don't
    # need to grasp any objects to find the dial location.
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial", close_gripper=True)
    # Once the gripper is around the dial, we can rotate the dial to the
    # right direction.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("in the right direction")