# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pulling against the window handle to open the window
    #  3. Pull the window open harder
    # To slide the window open to the left, the robot needs to grab the window handle from the right.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # Once the gripper is near the window handle, start pulling to slide the window open.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the robot's gripper is almost in front of the window handle, pull harder to open the window wider.
    if check("the robot's gripper is in front of the window handle"):
        robot.pull("window left harder")