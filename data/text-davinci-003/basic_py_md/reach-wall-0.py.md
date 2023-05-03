

```
# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    if check("the robot's gripper is above the wall and the robot's gripper is not near the goal"):
        robot.reach("around wall")
    if check("the robot's gripper is near the goal"):
        robot.reach("to goal")
```