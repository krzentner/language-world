

Steps:
1. Put gripper above plate
2. Push gripper into plate
3. Slide plate to goal

If the plate isn't below the gripper as seen from above, move the gripper above the plate.

```
if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with the plate"):
    robot.put("the gripper above the plate")
```

If the gripper is aligned with the plate but not near it, move the gripper down to the plate to slide it.

```
if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
    robot.push("the gripper into the plate")
```

If the gripper is near the plate, we've probably trapped the plate and can slide it to the target location.

```
if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
    robot.slide("the plate to the goal")
```