
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up the handle
    # First, get the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper is within the handle's range, we should be able to grab it.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle", close_gripper=True)
    # If the gripper is within the handle's range and closed, pull up the handle.
    if check("the robot's gripper is around the handle and the robot's gripper is closed"):
        robot.move_gripper("above the handle")