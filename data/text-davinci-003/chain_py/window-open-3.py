
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # To open the window we need to move the gripper near the window handle, on
    # the right side.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # If the gripper is near the window handle, we can start pushing the window
    # open.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the gripper is starting to be in front of the window handle, push harder.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")