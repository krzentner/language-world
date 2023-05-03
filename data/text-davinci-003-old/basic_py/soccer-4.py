
    if check("Ball is not centered and the robot's gripper is not vertically aligned with the ball"):
        robot.put("gripper in center of ball")
    if check("the robot's gripper is vertically aligned with the ball and the robot's gripper is not near the ball"):
        robot.push("gripper into the ball")
    if check("the robot's gripper is near the ball and the ball is not centered"):
        robot.pull("ball towards goal")
    if check("the ball is centered and the robot's gripper is near the ball"):
        robot.push("ball towards goal")