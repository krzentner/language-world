

Inside the function, we should first move the robot's gripper above the puck so we don't bump it while trying to grab it.

```
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal with a short wall in the way
    # First, put the gripper roughly above puck, so that we don't bump it while 
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
```

Next, we want to put the gripper around the puck if it isn't already.

```
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
```

Then, we try to close the gripper if it is near the puck and open.

```
    # If the gripper is near the puck and open, maybe we can grab it by closing 
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
```

Now that the gripper is closed, we want to move the puck to the goal. But in this case, there is a wall in between the gripper and the goal. To move the puck around the wall, we want to move it in a diagonal direction. 

```
    # We closed the gripper, and the puck is still near the gripper, so maybe we 
    # grabbed it.
    # Try to move the puck to the goal around the wall.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.push_diag("puck around wall to goal")
```

Finally, we make sure the puck is at the target location.

```
    # We pushed the puck around the wall, so make sure it is at the right
    # position.
    if check("puck is around the wall but not at goal"):
        robot.place("puck at goal")
```