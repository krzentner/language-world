

Steps:
  1. Put gripper above cube
  2. Drop gripper around cube
  3. Close gripper around cube
  4. Sweep cube to target location

If the robot's gripper is not above the cube, move the gripper above the cube.

```
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
```

If the robot's gripper is not around the cube, put it around the cube.

```
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
```

Once the gripper is near the cube and closed, move the gripper down to sweep the cube towards the target location.

```
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
```