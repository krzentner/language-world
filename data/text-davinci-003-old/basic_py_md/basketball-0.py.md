

If check("the robot's gripper is not above the basketball"):
    robot.put("gripper above basketball")
if check("the robot's gripper is near basketball and the robot's gripper is open"):
    robot.close("gripper around basketball")
if check("the robot's gripper is above basketball and the robot's gripper is closed"):
    robot.put("the basketball in front of the hoop")
if check("the basketball is in front of the hoop and the basketball is not above the hoop"):
    robot.push("the basketball into the hoop")