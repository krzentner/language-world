

Steps:
1. Put gripper above the puck
2. Drop gripper around the puck
3. Close the gripper around the puck
4. Move the puck to the target location

If the robot's gripper is not roughly above puck, move it there.
```
if check("the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck")
```

If the gripper is not around the puck, move it there.
```
if check("the robot's gripper is not around the puck and the robot's gripper is open"):
    robot.move_gripper("near the puck", close_gripper=True)
```

Once the gripper is near the puck and closed, move the puck to the target location.
```
if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
    robot.move_gripper("near the target location")
```