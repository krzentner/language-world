# window-open: slide the window open to the left
def window_open(robot):
    # First, put the gripper right of the window handle
    if check("the robot's gripper is not right of the window handle"):
        robot.move("gripper to the right of the window handle")
    # Once the gripper is in position, start pushing against the window handle
    if check("the robot's gripper is right of the window handle and the robot's gripper is not pushing against the window handle"):
        robot.push("against the window handle")
    # If the window is not fully open, push harder
    if check("the window is not fully open"):
        robot.push("harder")