

You may find the following commands useful:

```
robot.put("the robot's gripper is vertically aligned with the button")
robot.drop("the robot's gripper is aligned with button from the front")
robot.place("the robot's gripper is forward aligned with button")
robot.drop("the robot's gripper is vertically aligned with the button")
robot.put("gripper above button")
robot.place("gripper around button")
robot.drop("gripper on top of button")
robot.place("gripper against the front of the button")
robot.push("forward into button")
robot.grab("button")
robot.close("gripper around button")
robot.pull("button back")
robot.slide("button left")
robot.push("button right")
robot.place("gripper to the right of button")
robot.drop("gripper below button")
robot.place("gripper to the left of button")
robot.drop("gripper to the left of button")
robot.place("gripper above button")
robot.drop("gripper below button")
robot.place("gripper to the right of button")
robot.drop("gripper above button")
```

*/

# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not forward aligned with button"):
        robot.place("gripper above button")
    if check("the robot's gripper is above button and the robot's gripper is not forward aligned with button"):
        robot.place("gripper against the front of the button")
    if check("the robot's gripper is forward aligned with button and the robot's gripper is above button"):
        robot.drop("gripper on top of button")
    if check("the robot's gripper is forward aligned with button and the robot's gripper is above button"):
        robot.push("down on button")

# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not forward aligned with button"):
        robot.place("gripper above button")
    if check("the robot's gripper is forward aligned with button and the robot's gripper is above button"):
        robot.drop("gripper on top of button")
    if check("the robot's gripper is forward aligned with button and the robot's gripper is above button"):
        robot.push("down on button")

# button