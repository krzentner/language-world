

The steps for this task are as follows:

1. Put gripper above puck
2. Push gripper into top of puck
3. Slide puck to goal, pushing against the wall

First, put the gripper roughly above the puck, so that we don't bump it while trying to grab it.

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
    robot.move_gripper("near the wall")
```

Once the gripper is near the wall, we can move the puck towards the goal by pushing against the wall.

```
if check("the robot's gripper is near the wall"):
    robot.move_gripper("near the target location")
```