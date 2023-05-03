

Steps:
1. Put the gripper right of the window handle
2. Start pushing against the window handle to open the window
3. Push the window open harder

    if check("the robot's gripper is not right of the window handle"):
        robot.move_gripper("right of the window handle")
    
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")