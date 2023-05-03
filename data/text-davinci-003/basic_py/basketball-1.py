
    if check("the robot's gripper is not near basketball"):
        robot.go_to("basketball")
    if check("the robot's gripper is closed and not near basketball"):
        robot.put("gripper above basketball")
    if check("the robot's gripper is open and not near basketball"):
        robot.grab("basketball")
    if check("the robot's gripper is near hoop and basketball is not right of robot's gripper"):
        robot.put("gripper above hoop")
    if check("the robot's gripper is near hoop and basketball is right of robot's gripper"):
        robot.throw("basketball into hoop")