

Then add the following code:

```
if check("the robot's gripper is not near the ball"):
    robot.reach("to ball")
if check("the robot's gripper is not pre-grasped the ball"):
    robot.grasp("the ball")
if check("the robot's gripper has the ball and the hoop is not vertically aligned with the ball"):
    robot.align("hoop with ball")
if check("the robot's gripper is aligned with the hoop and the hoop is not within its reach"):
    robot.reach("to hoop")
if check("the robot's gripper is within reach of the hoop"):
    robot.release("ball into hoop")
```