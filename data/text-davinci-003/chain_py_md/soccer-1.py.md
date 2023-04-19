

Steps:
1. Put gripper above soccer ball
2. Push gripper into top of soccer ball
3. Slide soccer ball to goal

If the robot's gripper is not above the soccer ball, move the gripper above the soccer ball:

```
  if check("the robot's gripper is not above the soccer ball"):
      robot.put("gripper above soccer ball")
```

If the gripper is aligned with the soccer ball but not near it, move the gripper downward to the soccer ball to start sliding it:

```
  if check("the robot's gripper is vertically aligned with soccer ball and the robot's gripper is not near soccer ball"):
      robot.push("gripper into soccer ball")
```

If the gripper is near the soccer ball and the soccer ball is below the gripper, then close the gripper around the soccer ball and start sliding it:

```
  if check("the robot's gripper is near soccer ball and the soccer ball is below the robot's gripper"):
      robot.close("gripper around soccer ball")
      robot.slide("soccer ball to goal")
```