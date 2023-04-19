

If check("the robot's gripper is not above the soccer ball"):
    robot.place("gripper above soccer ball")
if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
    robot.drop("gripper around soccer ball")
if check("the robot's gripper is around the soccer ball and the soccer ball is not near goal"):
    robot.push("soccer ball towards goal")
if check("the robot's gripper is around the soccer ball and the soccer ball is near goal"):
    robot.slide("soccer ball into goal")