# basketball: put the ball into into the hoop
# def basketball(robot):
    if check("the robot's gripper is not above the ball and the ball is on the ground"):
        robot.place("gripper above ball")
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    if check("the robot's gripper is above ball and the robot's gripper is closed"):
        robot.push("ball into hoop")