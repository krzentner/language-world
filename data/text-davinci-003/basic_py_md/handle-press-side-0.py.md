

The program should look like this:

```
# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.align("gripper to handle")
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.push("down on handle")
```