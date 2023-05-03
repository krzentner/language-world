

Then complete the program:

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper over short wall")
    if check("the robot's gripper is vertically aligned with the top of the short wall"):
        robot.stretch("gripper over wall and above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```