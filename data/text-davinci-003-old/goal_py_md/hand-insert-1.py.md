

Steps:
1. Put the gripper above the puck
2. Drop the gripper around the puck
3. Close the gripper around the puck
4. Move the puck to the target location

If the robot's gripper is not above the puck, move it above the puck.
```
if check("the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck")
```

If the gripper isn't around the puck, put it around the puck.
```
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.move_gripper("near the puck", close_gripper=True)
```

If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
```
if check("the robot's gripper is above puck and the robot's gripper is closed"):
    robot.move_gripper("near the target location")
```