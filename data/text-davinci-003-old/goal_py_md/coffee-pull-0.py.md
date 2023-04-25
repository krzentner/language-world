

Steps:
1. Put gripper above mug handle
2. Drop gripper around mug handle
3. Pull mug to target location

If the robot's gripper is not above the mug handle, move it to the mug handle.
We don't need to be careful about the direction, since the mug is small and we're just pulling it (unlike when opening a drawer).

```
if check("the robot's gripper is not above the mug handle"):
    robot.move_gripper("above the mug handle")
```

Once the gripper is above the mug handle, we should be able to grab the mug handle by moving the gripper down around it. 

```
if check("the robot's gripper is above mug handle and the robot's gripper is not around mug handle"):
    robot.move_gripper("around the mug handle")
```

Once the gripper is around the mug handle, we can pull the mug to the target location.

```
if check("the robot's gripper is around mug handle"):
    robot.move_gripper("near the target location")
```