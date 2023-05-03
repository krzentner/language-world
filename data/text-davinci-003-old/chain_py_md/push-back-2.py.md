

Steps:
1. Put gripper behind puck
2. Push gripper into puck
3. Slide puck to goal

If the robot's gripper is not behind the puck, move the gripper behind it.

```
if check("the robot's gripper is not behind puck"):
    robot.put("gripper behind puck")
```

Once the gripper is behind the puck, push the gripper into it.

```
if check("the robot's gripper is behind the puck and the robot's gripper is not near the puck"):
    robot.push("gripper into puck")
```

Finally, slide the puck to the goal.

```
if check("the robot's gripper is near the puck and the puck is behind the robot's gripper"):
    robot.slide("puck to goal")
```