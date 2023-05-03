

    if check("the robot's gripper is not near the ball"):
        robot.put("gripper above ball")
    if check("the robot's gripper is near the ball and the robot's gripper is open"):
        robot.grab("ball")
    if check("the robot's gripper is closed around ball"):
        robot.move("gripper to hoop")
    if check("the robot's gripper is above hoop and the ball is below the hoop"):
        robot.lift("ball up to hoop")
    if check("the ball is above the hoop"):
        robot.align("ball in center of hoop")
    if check("the ball is in the center of hoop"):
        robot.release("ball")