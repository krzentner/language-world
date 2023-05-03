

Answer:

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not near the handle"):
        robot.reach("to handle")
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("down on handle")
```