# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pulling the window to the right to close it
    #  3. Close the window tighter by pulling harder
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper to the left of the window handle to start pulling
    if check("the robot's gripper is not left of the window handle"):
        robot.move_gripper("left of the window handle")
    # If the robot's gripper is left of the window handle we can probably slide the
    # window closed now by moving the gripper right.
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("vertically aligned with the window handle")