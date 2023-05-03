# Steps:
    #  1. Put gripper next to the handle
    #  2. Push the handle down from the side
    # First, put the gripper next to the handle.
    if check("the robot's gripper is not next to the handle"):
        robot.move_gripper("next to the handle")
    # Once the gripper is next to the handle, we can push down on the handle from
    # the side to press it.
    if check("the robot's gripper is next to the handle"):
        robot.move_gripper("near the target location")