

Then add your code to complete the task:

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is near the handle and the robot's gripper is not horizontally aligned with handle"):
        robot.align("the gripper with the handle")
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.push("down on handle")
```