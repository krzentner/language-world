# Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pulling on the window handle to open the window
    #  3. Pull the window open harder
    # If the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pulling.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # Once the gripper is near the window handle, grab the handle.
    # Then, pull it to open the window.
    if check("the robot's gripper is near the window handle"):
        robot.pull("window left")
    # If the robot's gripper is starting to be in front of the window handle,
    # pull harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.pull("window left harder")