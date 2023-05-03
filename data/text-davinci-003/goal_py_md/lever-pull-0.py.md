

Steps:
1. Put gripper right of the lever
2. Pull the lever up

If the robot's gripper is not near the lever, move it to the lever.
We don't need to be careful about the direction, since the lever is small and we're just pulling it.

```
    if check("the robot's gripper is not near the lever"):
        robot.move_gripper("near the lever")
```
    
Once the gripper is near the lever, we should be able to pull the lever up by moving the gripper left.

```
    if check("the robot's gripper is near the lever"):
        robot.move_gripper("left of lever")
```