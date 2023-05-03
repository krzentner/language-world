

Your program should check the conditions related to the robot's gripper, and have robot perform the required tasks accordingly. 

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the button and the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is not near the button and the robot's gripper is vertically aligned with button"):
        robot.push("gripper into button")
    if check("the robot's gripper is above the button and the button is below the robot's gripper"):
        robot.push("button down")