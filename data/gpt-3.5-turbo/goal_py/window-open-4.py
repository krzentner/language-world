# Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pulling the window open from the left side
    #  3. Continue pulling the window open until fully open
    # If the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pulling.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is right of the window handle, we can probably
    # start pulling the window open now by moving the gripper left.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # pull harder.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("left of the window handle")