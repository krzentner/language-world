
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper above handle down around it
    #  3. Pull handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper is lined up, we should be able to drop it around the handle
    # to grab it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.move_gripper("near the handle", close_gripper=True)
    # When the gripper is around the handle, we can just pull up the handle.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("above the handle")