

Steps:
1. Put gripper above the soccer ball
2. Push gripper down into the soccer ball
3. Slide soccer ball to the target location

If the robot's gripper is not above the soccer ball, move the gripper above the soccer ball.

```
if check("the robot's gripper is not above the soccer ball"):
    robot.put("gripper above the soccer ball")
``` 

If the gripper is aligned with the soccer ball, push the gripper into it in order to trap it.

```
if check("the robot's gripper is vertically aligned with the soccer ball")
    robot.push("gripper into the soccer ball")
```

Once the gripper is trapping the soccer ball, slide it to the target location

```
if check("the robot's gripper is trapping the soccer ball"):
    robot.slide("soccer ball to target location")
```