

The code for this specific task should look like this:

```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle and the handle is not left of the robot's gripper"):
        robot.grab("handle")
    if check("the handle is left of the robot's gripper and the robot's gripper is not near the handle"):
        robot.move("gripper to the handle")
    if check("the robot's gripper is near the handle"):
        robot.pull("up on the handle")
```