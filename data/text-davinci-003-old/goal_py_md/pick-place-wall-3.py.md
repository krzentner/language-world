

The steps for this task are as follows:

1. Put gripper above puck
2. Drop gripper around puck
3. Close gripper around puck
4. Move puck to goal while navigating around the wall

First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.

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
    robot.move_gripper("left of the wall")
```

If the gripper is left of the wall, we can move it up to the target location while avoiding the wall.

```
if check("the robot's gripper is left of the wall"):
    robot.move_gripper("around the wall and near the target location")
```

Once the gripper is near the target location, we can move it to the exact target location.

```
if check("the robot's gripper is near the target location"):
    robot.move_gripper("at the target location")
```