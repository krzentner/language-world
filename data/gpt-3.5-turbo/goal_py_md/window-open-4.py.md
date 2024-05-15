# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pulling the window handle towards the left to open the window
    #  3. Pull the window open harder
    # If the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pulling.
    if check("the window handle is not right of the robot's gripper"):
        robot.move_gripper("near the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open to the left by moving the gripper left.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the left end of the window"):
        robot.move_gripper("almost vertically aligned with the left end of the window")
    # If the robot's gripper is almost at the left end of the window,
    # pull harder to open it fully.
    if check("the robot's gripper is near the left end of the window"):
        robot.move_gripper("around the window handle")