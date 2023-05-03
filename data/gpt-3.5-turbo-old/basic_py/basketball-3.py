if check("the robot's gripper is not above the ball"):
        robot.place("gripper above the ball")
    if check("the ball is not inside the gripper and the robot's gripper is open"):
        robot.grab("the ball")
    if check("the ball is inside the gripper and the robot's gripper is closed"):
        robot.lift("the ball up")
    if check("the robot's gripper is above the hoop"):
        robot.drop("the ball into the hoop")