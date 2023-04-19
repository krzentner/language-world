

Steps:
1. Put gripper above cube 
2. Move the gripper down and around the cube
3. Close gripper around the cube
4. Move the cube to the target location

if check("the robot's gripper is not above the cube"):
    robot.put("gripper above cube")

if check("the robot's gripper is not around the cube and the robot's gripper is open"):
    robot.drop("gripper around cube")

if check("the robot's gripper is near the cube and the robot's gripper is open"):
    robot.close("gripper around cube")

if check("the robot's gripper is above the cube and the robot's gripper is closed"):
    robot.move("cube to goal")