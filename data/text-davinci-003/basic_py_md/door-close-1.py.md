

if check("the robot's gripper is not near the door handle"):
    robot.put("gripper above door handle")
if check("the robot's gripper is near the door handle and the robot's gripper is not around the door handle"):
    robot.put("gripper around door handle")
if check("the robot's gripper is around the door handle"):
    robot.push("door closed")