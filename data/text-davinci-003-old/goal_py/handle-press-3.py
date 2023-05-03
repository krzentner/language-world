
    # Steps:
    #  1. Put gripper above handle
    #  2. Push downwards on the handle
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # Once the gripper is aligned with the handle, we should be able to push the
    # handle down.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("near the handle")