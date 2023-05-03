 

The program should look like this:

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is to the left of the handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("down on handle")
```