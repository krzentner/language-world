
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Pull the window handle
    # If the window handle is left of the robot's gripper, move the gripper near
    # the window handle.
    if check("the robot's gripper is above the window handle"):
        robot.move_gripper("left of the window handle")
    # If the robot's gripper is near the window handle, start pushing it open by
    # moving it left.
    if check("the robot's gripper is left of the window handle and the robot's gripper is not around the window handle"):
        robot.move_gripper("around the window handle")
    # If the window handle is starting to align with the gripper, pull harder.
    if check("the robot's gripper is around the window handle"):
        robot.move_gripper("under the window handle")