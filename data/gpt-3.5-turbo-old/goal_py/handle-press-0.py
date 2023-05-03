# Steps:
    #  1. Line up the gripper above the handle
    #  2. Push down on the handle
    # First, line up the gripper vertically above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # Once the gripper is above the handle, push down on the handle.
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("near the handle")