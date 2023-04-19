

The robot should pick up the puck, hold it at the target location with a short wall in the way.

Steps:
1. Put gripper above puck
2. Drop gripper around puck
3. Close gripper around puck
4. Move puck to target location
5. Put gripper above wall
6. Push wall away
7. Move puck to goal

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
    robot.move_gripper("near the target location")
```

If the robot's gripper is near the target location, the robot should move the puck to the target location.

```
if check("the robot's gripper is near the target location"):
    robot.move_gripper("above the wall")
```

Once the robot's gripper is above the wall, it should push the wall away to make space for the puck.

```
if check("the robot's gripper is above the wall"):
    robot.move_gripper("away from the wall")
```

Finally, the robot should move the puck to the goal.

```
if check("the robot's gripper is away from the wall"):
    robot.move_gripper("near the target location")
```