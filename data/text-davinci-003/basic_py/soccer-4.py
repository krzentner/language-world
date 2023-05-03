
    if check("the robot's gripper is not near the soccer ball"):
        robot.put("gripper close to the soccer ball")
    if check("the robot's gripper is near the soccer ball and robot's gripper is open"):
        robot.close("gripper around soccer ball")
    if check("the robot's gripper is around the soccer ball and the goal is not in front of the robot's gripper"):
        robot.put("the goal in front of the gripper")
    if check("the goal is in front of the robot's gripper"):
        robot.kick("the soccer ball towards the goal")