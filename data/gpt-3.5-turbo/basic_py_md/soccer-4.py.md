# soccer: push the soccer ball into the target location
def soccer(robot):
    if check("the robot's gripper is not above the soccer ball"):
        robot.place("gripper above soccer ball")
    if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.drop("gripper around soccer ball")
    if check("the robot's gripper is near soccer ball and the robot's gripper is open"):
        robot.close("gripper around soccer ball")
    if check("the robot's gripper is above soccer ball and the robot's gripper is closed and the soccer ball is not touching the robot"):
        robot.push("soccer ball toward goal")
    if check("the soccer ball is touching the robot's gripper"):
        robot.lift("soccer ball")
    if check("the robot's gripper is above goal"):
        robot.place("soccer ball at goal")