
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is above the stick and the robot's gripper is not around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is around the stick and the robot's gripper is not in front of the thermos"):
        robot.move("stick in front of thermos")
    if check("the robot's gripper is in front of the thermos"):
        robot.push("the stick to pull the thermos to the goal")