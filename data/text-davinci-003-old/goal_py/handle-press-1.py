
    # Steps:
    #  1. Put gripper directly in front of the handle
    #  2. Push down on the handle
    # First put the gripper in front of the handle.
    if check("the robot's gripper is not forward aligned with the handle"):
        robot.move_gripper("forward aligned with the handle")
    # The gripper should now be in front of the handle. Push down on the handle
    # with the gripper.
    if check("not yet pushing down on handle"):
        robot.move_gripper("downwards")