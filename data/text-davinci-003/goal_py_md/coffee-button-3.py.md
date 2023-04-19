

Steps:
1. Put gripper in front of the button 
2. Line up the gripper vertically with the button 
3. Push down on the button from the top 

if check("the robot's gripper is not forward aligned with the button"): 
    robot.move_gripper("forward aligned with the button") 
if check("the robot's gripper is forward aligned with the button and the robot's gripper is not vertically aligned with the button"): 
    robot.move_gripper("vertically aligned with the button", close_gripper=True) 
if check("the robot's gripper is vertically aligned with the button"): 
    robot.move_gripper("near the button")