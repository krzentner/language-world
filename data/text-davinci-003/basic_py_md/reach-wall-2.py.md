

Then proceed to the function:

```
# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    if check("the robot's gripper is not above the wall"):
        robot.put("gripper above wall")
    if check("the robot's gripper is above the wall and the gripper is open"):
        robot.close("gripper around wall")
    if check("the robot's gripper is closed and the wall is below the robot's gripper"):
        robot.reachForward("over wall")
    if check("the robot's gripper is near the wall"):
        robot.reach("over wall and to goal")
```