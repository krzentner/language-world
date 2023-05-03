

The robot's gripper should move in a straight line from above it's current location to the goal.

```
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not above its goal"):
        robot.point("gripper at goal")
    if check("the robot's gripper is not forward aligned with the goal"):
        robot.align("gripper to goal")
    if check("the robot's gripper is above and aligned with the goal"):
        robot.put("gripper at goal")
``