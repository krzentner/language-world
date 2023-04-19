# Steps:
    #  1. Put gripper around the handle
    #  2. Lift the handle up
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, we can lift it up.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")