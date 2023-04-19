

Steps:
1. Put gripper near the cube
2. Grab the cube with the gripper
3. Move the gripper to the target bin
4. Put the cube down in the bin

if check("the robot's gripper is not near cube"):
    robot.move_gripper("near the cube", close_gripper=True):
    
if check("the robot's gripper is closed and near the cube"):
    robot.move_gripper("near the target bin")
    
if check("the robot's gripper is near the target bin"):
    robot.move_gripper("below the target bin", close_gripper=False)