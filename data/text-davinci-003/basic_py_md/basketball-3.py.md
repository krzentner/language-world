

Then add code to achieve the goal:

```
# basketball: put the ball into into the hoop
def basketball(robot):
    if check("the robot's gripper is not vertically aligned with the basketball"):
        robot.put("gripper above ball")
    if check("the robot's gripper is vertically aligned with the basketball and the robot's gripper is not around ball"):
        robot.grab("ball")
    if check("the robot's gripper is around the ball and the hoop is not horizontally aligned with the ball"):
        robot.align("ball to hoop")
    if check("the hoop is horizontally aligned with the ball and the ball is not near the hoop"):
        robot.move("ball to hoop")
    if check("the ball is near the hoop"):
        robot.push("push ball into hoop")
```