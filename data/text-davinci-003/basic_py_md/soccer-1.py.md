

If check("the robot's gripper is not near soccer ball"):
    robot.put("gripper above soccer ball")
if check("the robot's gripper is near soccer ball and the robot's gripper is not open"):
    robot.open("gripper around soccer ball")
if check("the robot's gripper is near soccer ball and the robot's gripper is open and the soccer ball is not below the robot's gripper"):
    robot.push ("gripper into soccer ball")
if check("the robot's gripper is near soccer ball and the soccer ball is below the robot's gripper"):
    robot.push("soccer ball to goal")