 

If check("the robot's gripper is not near the hoop"):
    robot.move("gripper to hoop")
if check("the robot's gripper is near the hoop"):
    robot.grab("the ball")
if check("the robot's gripper is holding the ball"):
    robot.align("gripper to center of hoop")
if check("the robot's gripper is centered with the hoop"):
    robot.throw("ball into hoop")