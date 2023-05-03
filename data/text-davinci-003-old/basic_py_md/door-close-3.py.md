

if check("the robot's gripper is not near the door handle"):
    robot.put("gripper above door handle")
if check("the robot's gripper is near the door handle and the robot's gripper is open"):
    robot.put("gripper around the door handle")
if check("the robot's gripper is vertically aligned with the door handle"):
    robot.push("door closed")