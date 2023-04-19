

Steps:
1. Put the gripper just above the button 
2. Push down gently on the button
   
    if check("the robot's gripper is not almost vertically aligned with the button"):
        robot.move_gripper("almost vertically aligned with the button")
    if check("the robot's gripper is almost vertically aligned with the button"):
        robot.move_gripper("near the button")