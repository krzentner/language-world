

Solution:

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is not right of the handle"):
        robot.put("gripper right of handle")
    if check("the robot's gripper is right of the handle and the robot's gripper is not near the handle"):
        robot.move("gripper near handle")
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle")
```