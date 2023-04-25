

Steps:
1. Put gripper above plate
2. Push gripper into plate
3. Slide plate to goal

If the robot's gripper is not above the plate, move it there.
```
if check("the robot's gripper is not above plate"):
    robot.put("gripper above plate")
```

If the gripper is above the plate but not near it, move the gripper down to the plate to slide it.
```
if check("the robot's gripper is above plate and the robot's gripper is not near plate"):
    robot.push("gripper into plate")
```

If the gripper is near the plate, we've probably trapped the plate and can slide it to the target location.
```
if check("the robot's gripper is near plate and the plate is below the robot's gripper"):
    robot.slide("plate to goal")
```