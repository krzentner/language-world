
    if check("the robot's gripper is not above soccer ball and the robot's gripper is not vertically aligned with the soccer ball"):
        robot.put("the gripper above the soccer ball")
    if check("the robot's gripper is vertically aligned with the soccer ball and the robot's gripper is not near soccer ball"):
        robot.push("the gripper into the soccer ball")
    if check("the robot's gripper is near the soccer ball and the ball is below the robot's gripper"):
        robot.slide("the soccer ball to the goal")