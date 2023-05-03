# soccer: push the soccer ball into the target location
def soccer(robot):
    if check("the robot's gripper is not above the soccer ball"):
        robot.put("gripper above soccer ball")
    if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.drop("gripper around soccer ball")
    if check("the robot's gripper is near the soccer ball and the robot's gripper is open"):
        robot.close("gripper around soccer ball")
    if check("the robot's gripper is above the soccer ball and the robot's gripper is closed"):
        robot.push("soccer ball to goal")