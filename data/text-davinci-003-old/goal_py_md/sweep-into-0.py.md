

Steps:
1. Put gripper above cube
2. Move gripper around cube until it is below the cube
3. Close gripper around cube
4. Sweep cube to goal

If the robot's gripper is not above the cube, move it above the cube.
```
if check("the robot's gripper is not above the cube"):
    robot.move_gripper("above the cube")
```

If the gripper is above the cube but not around it, move the gripper around the cube.
```
if check("the robot's gripper is above the cube and the robot's gripper is not around cube"):
    robot.move_gripper("around the cube", close_gripper=True)
```

If the gripper is around the cube, sweep it to the target location.
```
if check("the robot's gripper is around cube"):
    robot.move_gripper("near the target location")
```