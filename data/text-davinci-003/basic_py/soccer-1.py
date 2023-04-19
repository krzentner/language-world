
    if check("the robot's gripper is not above the soccer ball"):
        robot.put("gripper above soccer ball")
    if check("the robot's gripper is above the soccer ball and the robot's gripper is not near soccer ball"):
        robot.put("gripper to near soccer ball")
    if check("the robot's gripper is above soccer ball and the robot's gripper is near soccer ball"):
        robot.push("soccer ball to goal")