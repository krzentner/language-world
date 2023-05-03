
    if check("the robot's gripper is not above the basketball"):
        robot.place("gripper above the basketball")
    if check("the robot's gripper is above the basketball and the robot's gripper is not around the basketball"):
        robot.drop("gripper around basketball")
    if check("the robot's gripper is around basketball and the robot's gripper is open"):
        robot.close("gripper around basketball")
    if check("the robot's gripper is closed and the basketball is not below the hoop"):
        robot.place("basketball below hoop")
    if check("the basketball is below the hoop"):
        robot.release("basketball into hoop")