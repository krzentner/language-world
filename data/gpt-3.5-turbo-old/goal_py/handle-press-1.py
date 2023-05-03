# Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper is not around the handle, close the gripper around the handle.
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # If the gripper is around the handle, push down on the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("near the base of the handle")