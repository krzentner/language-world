    

Steps: 
1. Put gripper above cube
2. Drop gripper around cube
3. Close gripper around cube
4. Push the cube sideways to the target location

if check("the robot's gripper is not above the cube"):
    robot.place("gripper above cube")
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is near cube and the robot's gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is above cube and the robot's gripper is closed"):
    robot.push("cube sideways to target location")