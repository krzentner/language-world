if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is near ball"):
        robot.grab("ball")
    if check("the robot's gripper is above the hoop and the robot's gripper is holding the ball"):
        robot.dunk("ball into hoop")