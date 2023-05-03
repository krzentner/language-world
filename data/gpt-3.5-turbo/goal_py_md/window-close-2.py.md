# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pulling against the window handle to close the window
    #  3. Pull the window closed harder
    # If the robot's gripper is not close to the window handle, we should move the
    # gripper near the window handle to start pulling.
    if check("the robot's gripper is not near the window handle"):
        robot.move_gripper("above the window handle")
    # Once the gripper is near the window handle, we can start pulling the
    # window closed.
    if check("the robot's gripper is near the window handle and the robot's gripper is not behind the window handle"):
        robot.move_gripper("right of the window handle", close_gripper=True)
    # Finally, we can pull the window closed harder to make sure it's completely
    # closed.
    if check("the robot's gripper is behind the window handle"):
        robot.move_gripper("near the start position")