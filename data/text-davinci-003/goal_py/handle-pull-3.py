
    # Steps:
    #  1. Put gripper above handle
    #  2. Close gripper
    #  3. Pull up the handle
    # If the gripper isn't near the handle, put it near the handle.
    if check("the robot's gripper is not near handle"):
        robot.move_gripper("near the handle", close_gripper=True)
    # Now that the gripper is near the handle, close it to grab it.
    if check("the robot's gripper is near handle and the robot's gripper is closed"):
        robot.move_gripper("above the handle")
    # If the gripper is closed and above the handle, pull it up.
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("forward aligned with the handle")