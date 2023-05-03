

Solution:
```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the handle is not to the left of the robot's gripper"):
        robot.grab("handle")
    if check("the handle is to the left of the robot's gripper and the robot's gripper is not near the handle"):
        robot.pull("handle away from wall")
    if check("the robot's gripper is near the handle"):
        robot.up("gripper up")
```