Oops, it looks like you accidentally copied and pasted the code for the previous function. Here's the correct code for closing the window:

# window-close: slide the window closed to the right
# def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    # If the robot's gripper is starting to be behind the window handle,
    # push harder to close the window.
    if check("the robot's gripper is behind the window handle"):
        robot.push("window right harder")