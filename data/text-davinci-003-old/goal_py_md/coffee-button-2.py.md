

Then, the program should:

1. Put gripper above the button
2. Drop gripper around the button
3. Push down on the button

Steps:

1. Put gripper above the button: 
if check("the robot's gripper is not vertically aligned with button"):
    robot.move_gripper("vertically aligned with the button", close_gripper=True)
    
2. Drop gripper around the button: 
if check("the robot's gripper is vertically aligned with button and the robot's gripper is not around the button"):
    robot.move_gripper("around the button")

3. Push down on the button:
if check("the robot's gripper is around the button"):
    robot.move_gripper("near the button")