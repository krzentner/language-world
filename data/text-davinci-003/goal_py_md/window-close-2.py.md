

# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper to the left of the window handle
    #  2. Push the window closed
    #  3. Stop pushing the window when it is closed
    # We need to put the gripper to the left of the window handle before we can
    # push it closed.
    if check("the robot's gripper is not vertically aligned with the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # If the gripper is aligned with the window handle, then we can push it
    # closed.
    if check("the robot's gripper is vertically aligned with the window handle"):
        robot.move_gripper("right of the window handle")
    # Keep pushing the window until it is closed.
    if check("the window is not closed"):
        robot.move_gripper("left of the window handle")