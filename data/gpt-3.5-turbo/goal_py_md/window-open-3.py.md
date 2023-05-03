# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pulling on the window handle to open the window
    #  3. Pull the window open harder
    # If the the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pulling
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("left of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # pull harder.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("backwards aligned with the window handle")