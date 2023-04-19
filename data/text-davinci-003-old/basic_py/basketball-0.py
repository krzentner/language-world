
    if check("the robot's gripper is not horizontally aligned with the hoop"):
        robot.align("gripper to hoop")
    if check("the robot's gripper is not near the basketball"):
        robot.move("gripper near basketball")
    if check("the robot's gripper is above the basketball and the basketball is below the robot's gripper"):
        robot.drop("gripper around basketball")
    if check("the robot's gripper is around the basketball"):
        robot.throw("basketball into hoop")