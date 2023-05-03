if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    if check("the robot's gripper is not open and the robot's gripper is above the ball"):
        robot.open("gripper")
    if check("the robot's gripper is open and the robot's gripper is above the ball"):
        robot.grab("ball")
    if check("the robot's gripper is holding the ball and the robot's gripper is not aligned with the hoop"):
        robot.move("gripper above the hoop")
    if check("the robot's gripper is above the hoop and the robot's gripper is holding the ball"):
        robot.put("the ball into the hoop")