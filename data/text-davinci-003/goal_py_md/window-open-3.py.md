

1. Put gripper right of the window handle
2. Grab the window handle with the gripper
3. Start pushing against the window handle to open the window
4. Push open the window harder

# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    # 1. Put gripper right of the window handle
    # 2. Grab the window handle with the gripper
    # 3. Start pushing against the window handle to open the window
    # 4. Push open the window harder

    # First, move the gripper to the right of the window handle, so that the 
    # gripper can start pushing against the window.
    if check("the robot's gripper is not right of the window handle"):
        robot.move_gripper("right of the window handle")
    # Assuming the gripper is near the window, grab the window handle.
    # Make sure to close the gripper when grabbing the window handle.
    if check("the robot's gripper is right of the window handle"):
        robot.move_gripper("near the window handle", close_gripper=True)
    # Move the gripper back a bit to start pushing against the window handle.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("left of the window handle")
    # Push the window open harder by pushing the window handle farther.
    if check("the robot's gripper is almost vertically aligned with the window handle"):
        robot.move_gripper("vertically aligned with the window handle")