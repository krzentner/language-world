# basketball: put the ball into the hoop
def basketball(robot):
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    if check("the robot's gripper is above ball and the robot's gripper is closed"):
        if check("the robot is not near the basketball hoop"):
            robot.move("towards the basketball hoop")
        if check("the robot is near the basketball hoop"):
            robot.throw("the ball into the hoop")