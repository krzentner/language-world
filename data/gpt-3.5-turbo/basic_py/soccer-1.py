if check("the robot's gripper is not near the soccer ball"):
        robot.move("gripper to soccer ball")
    if check("the robot's gripper is near the soccer ball and the soccer ball is not below the robot's gripper"):
        robot.put("gripper below soccer ball")
    if check("the soccer ball is below the robot's gripper and the robot's gripper is closed"):
        robot.push("soccer ball to the goal")