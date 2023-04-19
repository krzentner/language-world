

Code:

```
# handle-pull: pull up the handle
# def handle_pull(robot):
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    if check("the robot's gripper is above handle and the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper vertically aligned with handle") 
    if check("the robot's gripper is above handle and the robot's gripper is vertically aligned with handle"):
        robot.pull("handle up")