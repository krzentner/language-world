

Your code should look something like this:
```
# basketball: put the ball into into the hoop
def basketball(robot):
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    if check("the robot's gripper is almost vertically aligned with ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is around the ball and the robot's gripper is not near hoop"):
        robot.move("to hoop")
    if check("the robot's gripper is near the hoop and the robot's gripper is closed"):
        robot.move("gripper up and above the hoop")
    if check("the robot's gripper is above the hoop"):
        robot.drop("ball into hoop")
```