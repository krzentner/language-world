

Steps:
  1. Put gripper above puck
  2. Push gripper into top of puck
  3. Slide puck to goal
  4. Move the wall out of the way

First, put the gripper above the puck, so that we don't bump it while trying to grab it.

If the robot's gripper is not above the puck, we can move it to the puck to begin pushing it.

```
if check("the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck")
```

If the gripper is above the puck, but the gripper isn't near the puck, move the gripper down to the puck to slide it.

```
if check("the robot's gripper is above puck and the robot's gripper is not near puck"):
    robot.move_gripper("above the puck", close_gripper=True)
```

If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location. However, we need to first move the wall out of the way.

We can pick the wall up with the gripper, move it to the side of the target location, and then return to the puck.

```
if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
    # Pick up the wall
    robot.move_gripper("above the wall")
    robot.move_gripper("above the wall", close_gripper=True)
    # Move the wall to the side of the target location
    robot.move_gripper("left of the target location")
    robot.move_gripper("above the target location", open_gripper=True)
    # Return to the puck
    robot.move_gripper("above the puck")
    robot.move_gripper("above the puck", close_gripper=True)
    # Push the puck to the target location
    robot.move_gripper("above the target location")
```

Finally, once the puck is near the target, we can open the gripper to let go of the puck.

```
if check("the robot's gripper is near the target location"):
    robot.move_gripper("above the target location", open_gripper=True)

```