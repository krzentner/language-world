
    # Steps:
    #  1. Put gripper near the wall
    #  2. Reach behind wall
    # Before we can reach the target location, we need to move the gripper near
    # the wall so it can reach behind it.
    if check("the robot's gripper is not near wall"):
        robot.move_gripper("near the wall")
    # Now that the gripper is near the wall, we can reach behind the wall to the
    # target location.
    if check("the robot's gripper is near wall"):
        robot.move_gripper("near the reach target")