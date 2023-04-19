
    # Steps:
    #  1. Put gripper slightly above handle
    #  2. Pull handle up
    # We should move the gripper above the handle so that we don't accidentally
    # press down on it.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.move_gripper("almost vertically aligned with handle")
    # If the gripper is lined up with the handle, start pulling.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("above the handle")