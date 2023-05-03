```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not above the button and the robot's gripper is not vertically aligned with the button"):
        robot.move("gripper above the button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
        robot.move("gripper near the button")
    if check("the robot's gripper is near the button and the robot's gripper is open"):
        robot.close("gripper around the button")
    if check("the robot's gripper is around the button"):
        robot.push("button down")
``` 

This code snippet should be able to execute the `button-press-topdown` task with the robot's gripper grabbing the button and pushing it down.