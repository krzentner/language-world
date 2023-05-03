

# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put the gripper to the left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # First, put the gripper near the window handle but to the left of it.
    if check("the robot's gripper is not bottom aligned with window handle and the robot's gripper is to the right of window handle"):
        robot.move("gripper to left of window handle")
    # If the gripper is near the window handle we can start to push the window
    # closed by moving the gripper right.
    if check("the robot's gripper is near window handle"):
        robot.slide("window right")
    # If the gripper is starting to be in front of the window handle,
    # push harder to close it.
    if check("the robot's gripper is in front of window handle"):
        robot.push("window right harder")