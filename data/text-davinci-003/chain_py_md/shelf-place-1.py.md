

Steps:
1. Put gripper above the block
2. Drop gripper around the block
3. Close gripper around the block
4. Move the block on top of the shelf

If the robot's gripper is not above the block, move the gripper above the block.

```
if check("the robot's gripper is not above the block"):
    robot.put("gripper above block")
```

If the robot's gripper is above the block, but not around the block, drop the 
gripper around the block.

```
if check("the robot's gripper is above the block and the robot's gripper is not around the block"):
    robot.drop("gripper around the block")
```

If the gripper is around the block, but not closed, close the gripper around the 
block.

```
if check("the robot's gripper is around the block and the robot's gripper is not closed"):
    robot.close("gripper around the block")
```

Once the gripper is closed around the block, we can move it on top of the shelf.

```
if check("the robot's gripper is around the block and the robot's gripper is closed"):
    robot.place("block on shelf")
```