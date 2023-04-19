
    if check("the robot's gripper is not above ball"):
        robot_put("gripper above ball")
    if check("the robot's gripper is above ball and the robot is not suspended above the goal"):
        robot.grab("the ball")
        robot.move("above the goal")
    if check("the robot is above the goal and the ball is not close to the goal"):
        robot.drop("the ball close to the goal")
    if check("the ball is close to the goal"):
        robot.throw("the ball towards the goal")