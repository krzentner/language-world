

It should look like this:

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is not forward aligned with handle"):
        robot.align("gripper with handle")
    if check("the robot's gripper is forward aligned with handle"):
        robot.push("handle down")
```