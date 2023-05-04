

If you want to do this task before completing the previous ones,
you can run `run-demo pick-place`.

## Explanation
We'll start off by putting the gripper above the puck, just like in `push`.
```
# Steps:
#  1. Put gripper above the puck
#  2. Grab the puck with the gripper
#  3. Line the puck up with the target location
#  4. Hold the puck in front of the target location
if check("the robot's gripper is not vertically aligned with the puck"):
    robot.move_gripper("vertically aligned with the puck")
```
Once the gripper is above the puck, we'll grab the puck by moving the gripper
closer.
The `open_gripper` parameter means to move the gripper, but keep the gripper open.
```
if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not above the puck"):
    robot.move_gripper("above the puck", open_gripper=True)
```
Once the gripper is above the puck, we'll line up the gripper with the target location.
The `close_gripper` parameter means to move the gripper, but close the gripper.
```
if check("the robot's gripper is not horizontally aligned with the target location and the robot's gripper is around the puck"):
    robot.move_gripper("horizontally aligned with the target location", close_gripper=True)
```
Finally, move the gripper to the target location.
We'll keep the gripper closed so it can hold the puck.
```
if check("the robot's gripper is not near the target location and the robot's gripper is horizontally aligned with the target location"):
    robot.move_gripper("near the target location", close_gripper=True)
```

```
# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Line the puck up with the target location
    #  4. Hold the puck in front of the target location
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    if check("the robot's grip