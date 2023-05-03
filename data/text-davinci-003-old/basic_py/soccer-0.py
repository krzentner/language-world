
    if check("the robot's gripper is not above the soccer ball and the robot's gripper is not vertically aligned with the soccer ball"):
        robot.put("gripper above soccer ball")
    if check("the robot's gripper is vertically aligned with the soccer ball and the robot's gripper is not near the soccer ball"):
        robot.push("gripper into soccer ball")
    if check("the robot's gripper is near the soccer ball and the soccer ball is below the robot's gripper"):
        robot.kick("soccer ball to goal")