

Steps:

1. Put gripper above soccer ball
2. Push gripper into soccer ball
3. Slide soccer ball to goal

If the robot's gripper is not above the soccer ball, move it above the soccer ball.

```
if check("the robot's gripper is not above soccer ball"):
    robot.put("gripper above soccer ball")
```

If the gripper is aligned with the soccer ball but not near it, move the gripper down to the soccer ball to slide it.

```
if check("the robot's gripper is vertically aligned with soccer ball and the robot's gripper is not near soccer ball"):
    robot.push("gripper into the soccer ball")
```

If the gripper is near the soccer ball, we've probably trapped the ball and can slide it to the target location.

```
if check("the robot's gripper is near the soccer ball and the soccer ball is below the robot's gripper"):
    robot.slide("soccer ball to the goal")
```