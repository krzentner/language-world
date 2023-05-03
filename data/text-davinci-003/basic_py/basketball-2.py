
    if check("the robot's gripper is near the basketball and the robot's gripper is not around the ball"):
        robot.grab("ball")
    if check("the robot's gripper is not near the hoop and the basketball is not vertically aligned with the hoop"):
        robot.put("ball above hoop")
        robot.align("ball with hoop")
    if check("the basketball is vertically aligned with the hoop"):
        robot.release("ball into hoop")