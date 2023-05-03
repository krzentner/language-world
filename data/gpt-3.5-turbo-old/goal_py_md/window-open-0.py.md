# window-open: slide the window open to the left
# def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    
    # First, put the gripper to the right of the window handle
    if check("the robot's gripper is not to the right of the window handle"):
        robot.move_gripper("to the right of the window handle")
        
    # Once the gripper is in the right position, start pushing against the window handle
    if check("the robot's gripper is to the right of the window handle and the robot's gripper is not touching the window handle"):
        robot.move_gripper("touching the window handle")
        
    # Push the window open harder
    if check("the robot's gripper is touching the window handle"):
        robot.move_gripper("to the left of the window handle")