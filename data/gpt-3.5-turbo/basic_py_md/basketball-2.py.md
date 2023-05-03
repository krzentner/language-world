# basketball: put the ball into into the hoop
def basketball(robot):
    if check("the robot's gripper is not near the ball"):
        robot.grab("ball")
    if check("the robot's gripper is near the ball and the ball is not at the right height for the hoop"):
        robot.lift("ball to hoop height")
    if check("the ball is at the right height for the hoop and the robot's gripper is not aligned with the hoop"):
        robot.move("gripper to hoop")
    if check("the robot's gripper is aligned with the hoop"):
        robot.drop("ball into hoop")