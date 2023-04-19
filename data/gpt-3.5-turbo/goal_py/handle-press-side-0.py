# Steps:
    #  1. Line up the gripper with the handle
    #  2. Push down on the handle from the side
    # We need to line up the gripper with the handle first.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once the gripper is near the handle, we can push down on the handle from
    # the side.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("horizontally aligned with the handle")