

Steps:
1. Put gripper above mug
2. Drop gripper around mug
3. Close gripper around mug
4. Pull mug to goal

If the robot's gripper is not above the mug, move it above the mug.
```
if check("the robot's gripper is not above the mug"):
    robot.put("gripper above mug")
```

If the robot's gripper is not around the mug, move it around the mug.
```
if check("the robot's gripper is not around the mug"):
    robot.drop("gripper around mug")
```

If the robot's gripper is near the mug, close the gripper around it.
```
if check("the robot's gripper is near the mug"):
    robot.close("gripper around mug")
```

If the robot's gripper is closed around the mug, pull the mug to the goal.
```
if check("the robot's gripper is closed around the mug"):
    robot.pull("mug to goal")
```