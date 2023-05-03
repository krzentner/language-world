

Here's the code:

```
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near target location"):
        robot.put("gripper near target location")