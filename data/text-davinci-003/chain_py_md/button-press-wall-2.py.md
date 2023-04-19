

Steps: 
1. Put the gripper horizontally in front of the button 
2. Push the wall aside to make room for the gripper
3. Push down on the button 

```
# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Put the gripper horizontally in front of the button
    #  2. Push the wall aside to make room for the gripper
    #  3. Push down on the button
    # Put the gripper horizontally in front of the button.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.put("gripper forward of button")
    # Now move the wall aside to make room for the gripper.
    if check("the wall is in the way of gripper"):
        robot.push("wall aside")
    # Now that the gripper can reach the button, push down on it.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")
```