

Steps:
1. Put gripper near the wall
2. Push against the wall
3. Move the puck to the target location

If the robot's gripper is not near the wall, move it to the wall. We don't need to be too precise, since we're just using the wall for support. 

```
if check("the robot's gripper is not near wall"):
    robot.move_gripper("near the wall")
```

Once the gripper is close to the wall, push against the wall by moving the gripper to the left. 

```
if check("the robot's gripper is near wall"):
    robot.move_gripper("left of the wall")
```

Now that the puck can move, slide it to the target location by moving the gripper to the target location while keeping the gripper pressed against the wall. 

```
if check("the robot's gripper is left of the wall and the puck is not near the target location"):
    robot.move_gripper("near the target location")
```