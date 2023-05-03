
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # We need to line up the gripper from the side before pushing
    # the window open.
    if check("the robot's gripper is not left of window handle"):
        robot.put("gripper right of window handle")
    # If the robot's gripper is near the window handle, we can
    # start sliding the window open.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # As the gripper slides further to the left, push harder to slide the window
    # further open.
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")