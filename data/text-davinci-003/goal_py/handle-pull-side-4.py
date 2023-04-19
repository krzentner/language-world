
    # Steps:
    #  1. Put gripper horizontally aligned with handle
    #  2. Pull up on the handle
    # We need to line up the gripper with the handle from the side so that it
    # can grip it.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.move_gripper("horizontally aligned with the handle", close_gripper=True)
    # Now that the gripper is lined up with the handle, pull up on the handle to
    # open the door.
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.move_gripper("above the handle")