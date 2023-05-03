

if check("the robot's gripper is not near the door handle"):
    robot.put("gripper above door handle")
if check("the robot's gripper is near the door handle and the robot's gripper is not around door handle"):
    robot.drop("gripper around door handle")
if check("the robot's gripper is around door handle"):
    robot.push("door closed")