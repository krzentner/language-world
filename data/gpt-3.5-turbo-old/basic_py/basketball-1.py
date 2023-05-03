if check("the robot's gripper is not near the ball"):
        robot.grab("the ball")
    if check("the robot's gripper is not aligned with the hoop"):
        robot.move("the gripper to be in front of the hoop")
    if check("the robot's gripper is aligned with the hoop and the robot's gripper is not high enough"):
        robot.move("the gripper up to the height of the hoop")
    if check("the robot's gripper is at the height of the hoop and the robot's gripper is not above the hoop"):
        robot.move("the gripper above the hoop")
    if check("the robot's gripper is above the hoop and the ball is not inside the hoop"):
        robot.drop("the ball into the hoop")