
    if check("the robot's gripper is not above the soccer ball"):
        robot.put("gripper above soccer ball")
    if check("the soccer ball is not below the robot's gripper"):
        robot.drop("gripper below soccer ball")
    if check("the robot's gripper is above the soccer ball and the robot's gripper is not near the soccer ball"):
        robot.align("gripper to the soccer ball")
    if check("the robot's gripper is near the soccer ball"):
        robot.slide("soccer ball to the goal")