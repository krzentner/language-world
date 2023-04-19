

if check("the robot's gripper is not near the cube"):
    robot.reach("to cube")
if check("the robot's gripper is not above the cube"):
    robot.put("gripper above cube")
if check("the robot's gripper is not around the cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is near the cube and the robot's gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is above the cube and the robot's gripper is closed"):
    robot.reach("to bin")
if check("the robot's gripper is not above the bin"):
    robot.put("gripper above bin")
if check("the robot's gripper is not around the cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is near the cube and the robot's gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is above the cube and the robot's gripper is closed"):
    robot.place("cube in bin")