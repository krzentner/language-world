

Solution:
```
#reach-wall: reach to the target location with a short wall in the way
#def reach_wall(robot):
    if check("the robot's gripper is not facing a short wall"):
        robot.reach("side of wall facing target")
    if check("the robot's gripper is facing a short wall"):
        robot.push("wall away from robot's path")
    if check("the robot's gripper is no longer facing the wall"):
        robot.reach("to goal")
```