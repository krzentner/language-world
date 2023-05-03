
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # To start sliding the window open, the robot must move the gripper to the
    # right of the window handle.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # To slide the window open, the robot must be able to push against the window
    # handle.
    # If the robot's gripper is just to the right of the window handle, start
    # pushing the window open.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the window handle is starting to be in front of the robot's gripper,
    # push harder.
    if check("the window handle is in front of the robot's gripper"):
        robot.push("window left harder")