# Steps:
    #  1. Put gripper around the handle
    #  2. Lift up on the handle
    # Because this is "pull", we just need to put the gripper around the handle.
    # Line up the robot's gripper with the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Now that the gripper is lined up with the handle, grab the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("lifted up the handle")