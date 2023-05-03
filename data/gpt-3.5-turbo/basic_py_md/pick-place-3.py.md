Sure! Here's a program to perform the `pick-place` task using the robot's single gripper:

```
# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.grab("puck")
    if check("the robot's gripper is not near the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is near the target location"):
        robot.put("gripper down at target location")
```

This code should work assuming the `put`, `grab`, `move`, and `check` functions used in the example code are correctly defined and implemented within the robot's system.