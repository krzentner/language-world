# window-open: slide the window open to the left
# def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder

    # First, check if the gripper is in position
    if check("the robot's gripper is not horizontally lined up with the window handle and the robot's gripper is not vertically aligned with the window handle"):
        robot.move("gripper to right of window handle")
    # If gripper is in position, start pushing the window handle
    elif check("the robot's gripper is horizontally lined up with the window handle and the window is not completely open"):
        robot.push("against the window handle")
        # If it's not sliding easily, push harder
        if check("the window is not sliding"):
            robot.push("window left harder")