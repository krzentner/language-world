

if check("the robot's gripper is not above the stick"):
    robot.put("gripper above stick")
if check("the robot's gripper is above the stick and the robot's gripper is not around stick"):
    robot.drop("gripper around stick")
if check("the robot's gripper is around the stick and the thermos is not in front of the robot's gripper"):
    robot.pull("stick towards thermos")
if check("the thermos is in front of the robot's gripper and the robot's gripper is not near the thermos"):
    robot.pull("stick towards thermos harder")
if check("the robot's gripper is near the thermos and the thermos is below the robot's gripper"):
    robot.pull("stick and thermos towards goal")