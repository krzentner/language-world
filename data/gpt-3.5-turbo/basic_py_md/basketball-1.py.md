# basketball: put the ball into into the hoop
# def basketball(robot):
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    if check("the robot's gripper is above ball and the ball is not in the hoop"):
        robot.throw("ball into the hoop")    # assumes "throw" method exists in robot class