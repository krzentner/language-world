if check("the robot's gripper is not vertically aligned with the basketball and the robot's gripper is not near the basketball"):
        robot.put("gripper above basketball")
    if check("the robot's gripper is near the basketball and the basketball is below the robot's gripper"):
        robot.grab("basketball")
    if check("the robot's gripper is vertically aligned with the hoop and the hoop is ahead of the robot's gripper"):
        robot.put("basketball into hoop")
    if check("the basketball is inside the hoop"):
        robot.release("basketball")