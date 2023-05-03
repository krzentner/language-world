if check("the robot's gripper is not near the soccer ball"):
        robot.move("gripper to soccer ball")
    if check("the robot's gripper is near the soccer ball and the robot's gripper is not around the soccer ball"):
        robot.grab("soccer ball")
    if check("the robot's gripper is around the soccer ball and the robot's gripper is not near the goal"):
        robot.move("gripper to goal")
    if check("the robot's gripper is near the goal"):
        robot.push("soccer ball into goal")