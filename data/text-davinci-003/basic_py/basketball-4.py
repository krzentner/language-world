
    if check("the robot's gripper is not near the ball"):
        robot.reach("near ball")  
    if check("the robot's gripper is not above ball and the robot's gripper is open"):
        robot.put("gripper above ball")
    if check("the robot's gripper is near the ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is around the ball and the ball is not near the hoop"):
        robot.put("ball near hoop")
    if check("the ball is below the hoop"):
        robot.lift("ball into hoop")