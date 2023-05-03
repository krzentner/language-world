

The robot needs to perform the following steps:
- Put gripper near the target location
- Approach the target location

```
# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Put gripper near the target location
    #  2. Approach the target location
    # First, put the gripper near the target location.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # Now that the gripper is close to the target, move the gripper towards it.
    if check("the robot's gripper is near the target location and the robot's gripper is not forward aligned with the target location"):
        robot.move_gripper("forward aligned with the target location")
```