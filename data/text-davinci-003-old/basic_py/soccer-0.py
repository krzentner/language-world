
    if check("the robot's gripper is not above the soccer ball"):
        robot.put("gripper above ball")
    if check("the robot's gripper is above the soccer ball and the robot's gripper is not near soccer ball"):
        robot.put("gripper near ball")
    if check("the robot's gripper is near the soccer ball"):
        robot.push("ball to goal")