

Steps:
1. Put gripper above lever
2. Grab the lever with the gripper
3. Rotate the lever up

If the robot's gripper is not near the lever, move the gripper to the lever.

```
    if check("the robot's gripper is not near the lever"):
        robot.move_gripper("near the lever", close_gripper=True)
```

Once the gripper is near the lever, rotate the gripper so that the gripper is facing the lever.

```
    if check("the robot's gripper is not facing the lever"):
        robot.move_gripper("facing the lever")
```

Once the gripper is facing the lever, pull up on the lever to rotate it.

```
    if check("the robot's gripper is facing the lever"):
        robot.move_gripper("above the lever")
```