# Steps:
    #  1. Put gripper near handle
    #  2. Turn gripper so that gripper fingers are aligned with handle
    #  3. Push the handle down
    # First, put the gripper near the handle
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the gripper fingers are not aligned with the handle, rotate the gripper
    # so that they are.
    if check("the gripper fingers are not aligned with the handle"):
        robot.rotate_gripper("aligned with the handle")
    # Once the gripper fingers are aligned, push the handle down.
    if check("the gripper fingers are aligned with the handle"):
        robot.move_gripper("down on the handle")