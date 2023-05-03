if check("the robot's gripper is not above the soccer ball"):
        robot.place("gripper above soccer ball")
    if check("the robot's gripper is not around the soccer ball and the robot's gripper is open"):
        robot.drop("gripper around soccer ball")
    if check("the robot's gripper is near the soccer ball and the robot's gripper is open"):
        robot.close("gripper around soccer ball")
    if check("the robot's gripper is above the soccer ball and the soccer ball is in front of the robot's gripper"):
        robot.push("soccer ball to goal")