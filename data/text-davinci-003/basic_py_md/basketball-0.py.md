

You can fill in the code below:

```
# basketball: put the ball into into the hoop
def basketball(robot):
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above the ball")
    if check("the robot's gripper is not around the basketball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is near the ball and the robot's gripper is open"):
        robot.close("gripper around the ball")
    if check("the robot's gripper is above the ball and the robot's gripper is closed"):
        robot.hold("ball in front of hoop")
    if check("the ball is not in front of the hoop and the robot's gripper is closed"):
        robot.swing("gripper basketball toward the hoop")
    if check("the ball is above the hoop and the robot's gripper is closed"):
        robot.toss("gripper basketball into the hoop")
``