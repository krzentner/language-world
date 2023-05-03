

Steps:
  1. Put gripper above the plate
  2. Line up the plate with the target
  3. Slide the plate sideways into the target location
  
We should put the gripper above the plate before trying to slide it, because the plate's edges are sharp and the robot's gripper is too broad to line up with just one of the plate's corners.

If the plate isn't left of the gripper, we should put the gripper above the plate.

```
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
```

Now that the gripper's above the plate, we need to make sure the plate is lined up with the target by moving the gripper to the left.

```
    if check("the robot's gripper is above the plate and the plate is not horizontally aligned with target"):
        robot.move_gripper("horizontally aligned with the target")
```

Once the gripper is lined up with the target, the robot can slide the plate sideways into the target location.

```
    if check("the robot's gripper is horizontally aligned with the target and the plate is not sideways aligned with the target"):
        robot.move_gripper("sideways aligned with the target")
```