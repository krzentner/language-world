

Steps:
1. Put gripper around the drawer handle
2. Pull the drawer open

If the gripper isn't near the drawer handle, move it there.
We want to make sure we're not too far up, so we check the position relative to the handle itself.

```
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
```

If the robot's gripper is near the drawer handle, start pulling the drawer open by moving to the left. The drawer is a wide object, so we need to check if the handle is in front of the gripper, not around it.

```
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("left of the drawer handle")
```