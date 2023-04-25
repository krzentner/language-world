

Steps:
1. Put the gripper above the cube 
2. Drop the gripper around the cube 
3. Close the gripper around the cube 
4. Move the cube towards the target bin 
5. Place the cube into the bin 

if check("the robot's gripper is not above the cube"):
    robot.put("gripper above cube")
if check("the robot's gripper is not around the cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is near the cube and the robot's gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is above the cube and the robot's gripper is closed"):
    robot.move("cube towards target bin")
if check("the robot's gripper is near the target bin and the robot's gripper is closed"):
    robot.place("cube into target bin")