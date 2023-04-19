

if check("the robot's gripper is not near the basketball"):
    robot.move("gripper to ball")
if check("the robot's gripper is above the basketball and the robot's gripper is not around the basketball"):
    robot.drop("gripper around basketball")
if check("the robot's gripper is around the basketball and the robot's gripper is not near the hoop"):
    robot.move("gripper to hoop")
if check("the basketball is near the hoop and the robot's gripper is open"):
    robot.close("gripper around ball")
if check("the robot's gripper is around the basketball and the hoop is below the robot's gripper"):
    robot.lift("ball to hoop")
if check("the hoop is above the robot's gripper and the robot's gripper is closed"):
    robot.drop("ball into hoop")