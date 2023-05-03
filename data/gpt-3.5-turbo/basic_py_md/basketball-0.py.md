# basketball: put the ball into the hoop
def basketball(robot):
    if check("the robot's gripper is not near the ball"):
        robot.grab("the ball")
    if check("the robot has the ball"):
        robot.put("the ball near the hoop")
    if check("the ball is near the hoop"):
        robot.throw("the ball into the hoop")