# reach: reach to the target location
# def reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

To perform the `reach` task, we simply move the robot's gripper directly to the target location. We only need to check if the gripper is not already near the target. If that's the case, we move the gripper to the goal.

Here's the code for the `reach` task:

```
# reach: reach to the target location
# def reach(robot):
    # Steps:
    #  1. Reach towards the target
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")
```