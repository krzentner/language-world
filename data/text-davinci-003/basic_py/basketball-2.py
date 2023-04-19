
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    if check("ball is not left of the robot's gripper and ball is not forward aligned with the robot's gripper"):
        robot.grab("ball")
    if check("the robot's gripper is forward aligned with the ball and the ball is not above the target"):
        robot.aim("ball at target")
    if check("the ball is just above the target"):
        robot.drop("ball into goal")