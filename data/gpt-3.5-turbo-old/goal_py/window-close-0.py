# Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is near the window handle and is not above the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the gripper is above the window handle, close the gripper to hold onto
    # the window handle, and push the window closed.
    if check("the robot's gripper is above the window handle and the robot's gripper is not closed"):
        robot.move_gripper("near the window handle", close_gripper=True)