# Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pulling the window handle to open the window
    #  3. Pull the window open harder
    # If the window handle is left of the robot's gripper, move the gripper near
    # the window handle to start pulling it open
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # If the gripper is now near the handle, we can probably start sliding the
    # window open by moving the gripper left.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the grip is starting to be behind the window handle, pull harder
    if check("the robot's gripper is behind the window handle"):
        robot.pull("window left harder")