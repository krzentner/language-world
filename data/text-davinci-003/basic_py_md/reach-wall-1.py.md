

Then fill in the logic:

```
# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    if check("the robot's gripper is not near the target location"):
        robot.move("gripper to left of reach target")
    if check("the robot's gripper is not in front of wall and the robot's gripper is not above wall"):
        robot.put("the gripper above the wall")
    if check("the robot's gripper is above wall"):
        robot.push("wall away")
    if check("the gripper is in front of wall and the gripper is near the reach target"):
        robot.reach("to goal")
```