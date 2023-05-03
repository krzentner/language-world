# Steps:
    #  1. Put gripper above the handle
    #  2. Push down on the handle
    # Place the gripper above the handle before pushing.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # Push down on the handle.
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("on the handle")