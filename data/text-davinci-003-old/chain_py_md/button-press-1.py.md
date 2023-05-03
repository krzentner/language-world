

Steps:
1. Put the gripper in front of the button 
2. Nudge the button 
3. Push down on the button 

```
# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Put gripper in front of button
    #  2. Nudge the button 
    #  3. Push down on the button 
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper in front of button")
    if check("the robot's gripper is horizontally aligned with button"):
        robot.nudge("button")
    if check("the robot's gripper is still horizontally aligned with button"):
        robot.push("down on button")
```