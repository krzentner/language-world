

Steps:
  1. Put gripper around plate 
  2. Slide plate to the target location 

First, we need to put the gripper around the plate.
If the robot's gripper is not near the plate, move it to the plate. 
We don't have to be line the gripper up with the plate carefully, since we're sliding the plate.

```
if check("the robot's gripper is not near plate"):
    robot.move_gripper("near the plate")
```

Once the gripper is near the plate, close the gripper to grab the plate.

```
if check("the robot's gripper is near plate"):
    robot.move_gripper("near the plate", close_gripper=True)
```

To slide the plate back to the target location, we need to line up the gripper with the target location.

```
if check("the robot's gripper is not horizontally aligned with the target location"):
    robot.move_gripper("horizontally aligned with the target location")
```

Now the plate should be aligned with the goal and we can slide it back. 

```
if check("the robot's gripper is horizontally aligned with the target location"):
    robot.move_gripper("above the plate")
```