
    if check("the robot's gripper is not above the basketball"):
        robot.place("gripper above basketball")
    if check("the robot's gripper is not forward aligned with hoop"):
        robot.align("gripper to hoop")
    if check("the robot's gripper is not horizontally aligned with hoop"):
        robot.align("basketball to hoop")
    if check("basketball is horizontally aligned with hoop and the robot's gripper is closed"):
        robot.push("basketball into hoop")