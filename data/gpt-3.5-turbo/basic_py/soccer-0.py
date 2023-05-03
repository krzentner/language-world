if check("the robot's gripper is not near the soccer ball and the robot's gripper is not vertically aligned with the soccer ball"):
        robot.put("the gripper above the soccer ball")
    if check("the robot's gripper is vertically aligned with the soccer ball and the robot's gripper is not around the ball"):
        robot.grab("the soccer ball")
    if check("the robot's gripper is around the soccer ball and the ball is not near the goal"):
        robot.push("the ball towards goal")
    if check("the ball is near the goal"):
        robot.release("the soccer ball at goal")