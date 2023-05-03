
    if check("the robot's gripper is not above the soccer ball"):
        robot.put("gripper above soccer ball")
    if check("the robot's gripper is above the soccer ball and the robot's gripper is not near soccer ball"):
        robot.push("gripper into soccer ball")
    if check("the robot's gripper is near the soccer ball and the soccer ball is not aligned with the goal location"):
        robot.align("soccer ball to goal")
    if check("the soccer ball is aligned with the goal location"):
        robot.push("soccer ball to goal")