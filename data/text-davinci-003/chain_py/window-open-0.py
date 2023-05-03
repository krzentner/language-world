
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # Move the gripper left, catching the window handle and starting to open it.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the window handle is hard to open, push harder.
    if check("the window handle is hard to open"):
        robot.push("window left harder")