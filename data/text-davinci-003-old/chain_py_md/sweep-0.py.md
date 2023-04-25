

Steps:
1. Put gripper above cube
2. Grab cube with gripper
3. Move cube to the left/right
4. Push cube to target location

If the robot's gripper is not above the cube, we should move the gripper above the cube.

```
if check("the robot's gripper is not above the cube"):
    robot.put("gripper above cube")
```

If the gripper is above the cube, we can grab it by closing the gripper around the cube.

```
if check("the robot's gripper is above the cube and the robot's gripper is open"):
    robot.close("gripper around cube")
```

If the gripper is closed around the cube, we can move it to the left or right.

```
if check("the robot's gripper is closed around the cube"):
    robot.move("cube left/right")
```

If the cube is near the target location, we can push it to the target location.

```
if check("the cube is near the target location"):
    robot.push("cube to target location")
```