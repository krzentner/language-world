
    # Steps:
    #  1. Put the gripper above the handle
    #  2. Put the gripper around the handle
    #  3. Twist the handle to the left
    # First, put the gripper slightly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle", close_gripper=True)
    # If the gripper is still not around the handle, center it with the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, turn it left.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("near the handle")