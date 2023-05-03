# basketball: put the ball into into the hoop
def basketball(robot):
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    if check("the robot's gripper is above ball and the robot's gripper is closed"):
        if check("the robot's arm is not extended toward the hoop"):
            robot.reach("to hoop")
        if check("the robot's arm is extended toward the hoop and the ball is not near the hoop"):
            robot.slide("ball to the hoop")
        if check("the ball is near the hoop"):
            robot.push("ball into the hoop")