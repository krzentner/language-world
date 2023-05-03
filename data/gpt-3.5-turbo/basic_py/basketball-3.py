if check("the robot's gripper is not near the ball"):
        robot.place("gripper above ball")
    if check("the robot's gripper is near the ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    if check("the ball is in the robot's gripper and the robot's gripper is above the hoop"):
        robot.throw("ball into hoop")