
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not near the window handle or not aligned with it
    # vertically, we should move the gripper near the window handle so that we can
    # start pushing.
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is to the right of the window handle"):
        robot.move("gripper to left of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window closed now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    # If the robot's gripper is starting to be in back of the window handle,
    # push harder.
    if check("the robot's gripper is in back of the window handle"):
        robot.push("window right harder")