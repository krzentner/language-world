
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    if check("the robot's gripper is above the ball and the ball is not inside the hoop"):
        robot.drop("ball into hoop")
    if check("the ball is inside the hoop and the hoop is not open"):
        robot.push("ball into hoop")