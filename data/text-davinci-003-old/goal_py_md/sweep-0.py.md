

Steps:
1. Put gripper above cube
2. Drop gripper around cube
3. Close gripper around cube
4. Sweep cube to the target location

If the robot's gripper is not above the cube, move it above the cube.
```
if check("the robot's gripper is not above the cube"):
    robot.move_gripper("above the cube")
```

If the gripper is not around the cube, put it around the cube.
```
if check("the robot's gripper is not around the cube and the robot's gripper is open"):
    robot.move_gripper("near the cube", close_gripper=True)
```

Once the gripper has the cube, sweep the cube to the target location.
```
if check("the robot's gripper is around the cube"):
    robot.move_gripper("near the target location")
```