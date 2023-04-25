

Steps:
1. Put the gripper above the puck
2. Drop the gripper around the puck
3. Move the puck to the target location

If the robot's gripper is not above the puck, move it to the puck.
```
if check("the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck")
```

If the gripper isn't around the puck, put it around the puck.
```
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.move_gripper("near the puck", close_gripper=True)
```

Once the gripper is around the puck, move it to the target location.
```
if check("the robot's gripper is around puck"):
    robot.move_gripper("near the target location")
```