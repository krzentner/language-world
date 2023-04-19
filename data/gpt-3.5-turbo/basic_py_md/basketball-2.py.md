# basketball: put the ball into the hoop
# def basketball(robot):

def basketball(robot):
    if check("the robot's gripper is not near the ball"):
        robot.reach("to the ball")
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is near the ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    if check("the robot's gripper is above hoop and the robot's gripper is closed"):
        robot.put("ball into hoop")