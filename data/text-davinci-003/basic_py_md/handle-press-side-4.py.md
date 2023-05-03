

The program should then contain:

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.put("gripper beside handle")
    if check("the robot's gripper is horizontally aligned with handle and the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above handle"):
        robot.push("down on handle")
```