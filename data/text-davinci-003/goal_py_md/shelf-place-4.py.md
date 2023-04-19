

Steps:
1. Put gripper above the block
2. Drop gripper around the block
3. Close gripper around the block
4. Move block to goal

If the robot's gripper is not above the block, move it above the block.
```
if check("the robot's gripper is not above the block"):
    robot.move_gripper("above the block")
```

If the gripper isn't around the block, move it around the block.
```
if check("the robot's gripper is not around block and the robot's gripper is open"):
    robot.move_gripper("near the block", close_gripper=True)
```

If the gripper is near the block and open, close the gripper to grab the block.
```
if check("the robot's gripper is near the block and the robot's gripper is closed"):
    robot.move_gripper("near the goal")
```

If the gripper is near the target location with the block, move the gripper away from the block to release it.
```
if check("the robot's gripper is near the goal and the robot's gripper is open"):
    robot.move_gripper("away from the block")
```