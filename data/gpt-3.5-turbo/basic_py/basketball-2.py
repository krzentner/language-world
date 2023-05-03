if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    if check("the robot's gripper is open"):
        robot.close("gripper around ball")
    if check("the robot's gripper is around the ball and the robot's gripper is not above the hoop"):
        robot.lift("ball toward the hoop")
    if check("the robot's gripper is above the hoop"):
        robot.drop("ball into the hoop")