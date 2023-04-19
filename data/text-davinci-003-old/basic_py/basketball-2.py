
    if check("the robot's gripper is not near the basketball and the robot's gripper is open"):
        robot.place("gripper near basketball")
    if check("the robot's gripper is near the basketball and the robot's gripper is open"):
        robot.grab("basketball")
    if check("the robot's gripper is near the basketball and the robot's gripper is closed"):
        robot.aim("basketball at hoop")
    if check("the basketball is aimed at the hoop"):
        robot.throw("basketball at hoop")