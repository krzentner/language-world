if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    if check("the robot's gripper is open and not around the ball"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is around the ball and the ball is not aligned with the hoop"):
        robot.move("the ball towards the hoop")
    if check("the ball is aligned with the hoop and the robot's gripper is around the ball"):
        robot.push("the ball into the hoop")