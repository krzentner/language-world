
    # Steps:
    #  1. Reach towards the target
    #  2. Push the wall aside
    #  3. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location.
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")
    # If the robot's gripper is blocked by a wall, use the gripper to push it
    # aside.
    if check("the robot's gripper is blocked by a wall"):
        robot.move_gripper("to the side of the wall")
    # Once the wall is pushed aside, the robot's gripper should be able to reach
    # the target location.
    if check("the robot's gripper is not near reach target and the wall is pushed aside"):
        robot.move_gripper("near the reach target")