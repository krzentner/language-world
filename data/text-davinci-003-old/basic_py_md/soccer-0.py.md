

If check("the robot's gripper is not above the soccer ball"):
    robot.put("gripper above the soccer ball")
if check("the robot's gripper is not forward aligned with the soccer ball"):
    robot.align("gripper with soccer ball")
if check("the robot's gripper is not near the soccer ball"):
    robot.slide("gripper into soccer ball")
if check("the soccer ball is not near the goal"):
    robot.push("soccer ball to goal")