

Then write the code:

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above the handle")
    if check("the robot's gripper is vertically aligned with the handle, and the robot's gripper is not near handle"):
        robot.move("gripper to side of handle")
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle")
```