if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    if check("the ball is not in the robot's gripper and the gripper is open"):
        robot.pick("the ball with the gripper")
    if check("the ball is in the robot's gripper and the gripper is closed and the robot's gripper is above the hoop"):
        robot.drop("the ball into the hoop")