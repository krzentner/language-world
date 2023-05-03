

Steps:
1. Put the gripper right of the cube
2. Drop the gripper around the cube
3. Close gripper around the cube
4. Swing the cube to the right to the target location

if check("the robot's gripper is not right of the cube"):
    robot.move_gripper("right of the cube", close_gripper=True)
if check("the robot's gripper is not around the cube"):
    robot.move_gripper("around the cube")
if check("the robot's gripper is around the cube and the robot's gripper is not closed"):
    robot.move_gripper("closed")
if check("the robot's gripper is around the cube and the robot's gripper is closed"):
    robot.move_gripper("right of the target location")