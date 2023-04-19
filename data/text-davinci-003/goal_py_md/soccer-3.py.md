

Steps:
1. Put gripper above the soccer ball 
2. Push gripper into top of soccer ball 
3. Slide soccer ball to target location 

If the robot's gripper is not above the soccer ball, move the gripper to be vertically aligned with the soccer ball.

```
if check("the robot's gripper is not above the soccer ball"):
    robot.move_gripper("vertically aligned with the soccer ball")
```

If the gripper is aligned with the soccer ball but not near it, we can move the gripper down to the soccer ball and trap it before pushing it to the target location.

```
if check("the robot's gripper is vertically aligned with the soccer ball and the robot's gripper is not near soccer ball"):
    robot.move_gripper("above the soccer ball", close_gripper=True)
```

If the gripper is near the soccer ball, we can slide the soccer ball to the target location.

```
if check("the robot's gripper is near the soccer ball and the soccer ball is below the robot's gripper"):
    robot.move_gripper("above the target location")
```