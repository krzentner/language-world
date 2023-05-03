

if check("the robot's gripper is not above stick"):
    robot.put("gripper above stick")
if check("the robot's gripper is not around stick and the robot's gripper is open"):
    robot.drop("gripper around stick")
if check("the robot's gripper is near the stick and the robot's gripper is closed"):
    robot.put("stick on thermos")
if check("the robot's gripper is above the stick and the robot's gripper is open"):
    robot.push("stick to goal")