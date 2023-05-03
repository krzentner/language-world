

Solution:

```
# basketball: put the ball into into the hoop
# def basketball(robot):
    if check("the robot's gripper is not above the ball"):
        robot.reach("above the ball")
    if check("the robot's gripper is above the ball and the robot's gripper is open"):
        robot.grab("the ball")
    if check("the robot's gripper is above the ball and the robot's gripper is closed"):
        robot.reach("above the basket")
    if check("the robot's gripper is close to the hoop and the ball is below the hoop"):
        robot.drop("the ball into the hoop")
```