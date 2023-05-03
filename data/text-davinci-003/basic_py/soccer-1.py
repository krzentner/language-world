
    if check("the robot's gripper is not above the soccer ball"):
        robot.place("gripper above soccer ball")
    if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.drop("gripper around soccer ball")
    if check("the robot's gripper is near soccer ball and the robot's gripper is open"):
        robot.close("gripper around the soccer ball")
    if check("the robot's gripper is above soccer ball and the robot's gripper is closed"):
        robot.push("forward Soccer ball to goal")