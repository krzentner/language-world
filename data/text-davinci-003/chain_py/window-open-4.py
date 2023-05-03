
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # To start slidng the window open, we should move the gripper near the
    # window handle.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # Once the robot's gripper is near the window handle we can probably slide
    # the window open by pushing left.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the robot's gripper starts to be behind the window handle, it means we
    # need to push harder.
    if check("the robot's gripper is behind the window handle"):
        robot.push("window left harder")