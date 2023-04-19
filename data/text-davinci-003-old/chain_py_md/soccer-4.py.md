

Steps:
1. Put gripper near the soccer ball
2. Push the ball towards the target location

if check("the robot's gripper is not near the soccer ball"):
    robot.put("gripper near soccer ball")

if check("the robot's gripper is near the soccer ball"):
    robot.push("ball towards target location")