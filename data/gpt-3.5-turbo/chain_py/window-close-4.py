# Steps:
    #  1. Put gripper above the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not directly above the window handle, we should
    # move the gripper to be above the window handle before starting to push
    if check("the robot's gripper is not vertically aligned with the window handle"):
        robot.move("gripper above window handle")
    # If the gripper is above the window handle, we can start pushing it to the
    # right to close the window.
    if check("the robot's gripper is above the window handle"):
        robot.slide("window right")
    # If the robot's gripper is starting to be to the left of the window handle,
    # push harder.
    if check("the robot's gripper is to the left of the window handle"):
        robot.push("window right harder")