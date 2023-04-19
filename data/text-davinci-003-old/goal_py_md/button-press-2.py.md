

Steps:
1. Put the gripper near the button
2. Line up the gripper so it is forward aligned with the button
3. Push the button down

if check("the robot's gripper is not near the button"):
    robot.move_gripper("near the button")
if check("the robot's gripper is not forward aligned with the button"):
    robot.move_gripper("forward aligned with the button")
if check("the robot's gripper is forward aligned with the button"):
    robot.move_gripper("downward aligned with the button")