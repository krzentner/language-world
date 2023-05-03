

The task consists of:
1. Put the gripper above the wall
2. Lever the wall up by pushing against it with the gripper
3. Move the gripper above the puck
4. Push gripper into top of puck
5. Slide puck to goal

First, put the gripper above the wall, so that the gripper can move the wall out of the way.
```
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
```

Now that the gripper is above the wall, lever the wall up by pushing down against it.
```
    if check("the robot's gripper is above the wall"):
        robot.move_gripper("down against the wall")
```

Once the wall is out of the way, move the gripper above the puck.
```
    if check("the robot's gripper is barely above the wall"):
        robot.move_gripper("above the puck")
```

If the gripper isn't near the puck, move it near the puck.
```
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
```

If the gripper is near the puck, we can push it down to trap it.
```
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("down into the puck", close_gripper=True)
```

Once the puck is trapped, move the gripper above the target location.
```
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")
```