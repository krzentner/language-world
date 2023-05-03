# Steps:
    #  1. Put gripper next to the handle
    #  2. Push down the handle
    # We need to place the gripper next to the handle before we can push it.
    if check("the robot's gripper is not next to the handle"):
        robot.move_gripper("next to the handle")
    # Once the gripper is next to the handle, we can just push it down.
    if check("the robot's gripper is next to the handle"):
        robot.move_gripper("near the target location")