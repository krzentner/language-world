

Steps:
1. Put gripper above puck
2. Push gripper into top of puck
3. Slide puck to goal, pushing against the wall

The first two steps are the same as a regular push, so we can just copy that code.

If the puck isn't below the gripper as seen from above, move the gripper above the puck.

```
if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
    robot.move_gripper("vertically aligned with the puck")
```

If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.

```
if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
    robot.move_gripper("above the puck", close_gripper=True)
```

Now the gripper is near the puck and can push against the wall. To do this, check if the puck is close to the wall, and if so, move the gripper left to push against the wall.

```
if check("the robot's gripper is near the puck and the puck is close to the wall"):
    robot.move_gripper("left of the puck")
```

Once the puck is clear of the wall, move the gripper above the target location.

```
if check("the robot's gripper is near the puck and the puck is not close to the wall"):
    robot.move_gripper("above the target location")
```