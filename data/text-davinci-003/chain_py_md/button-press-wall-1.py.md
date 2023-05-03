

Steps: 
1. Put gripper slightly above and to the right of the button
2. Push gripper into button while pushing against the wall
3. Slide gripper to the right, pushing against the button

```
# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Put gripper slightly above and to the right of the button
    #  2. Push gripper into button while pushing against the wall
    #  3. Slide gripper to the right, pushing against the button
    # Put the gripper above and to the right of the button, since the wall is in
    # the way.
    if check("the robot's gripper is not above and to the right of the button"):
        robot.place("gripper slightly above and to the right of button")
    # Once the gripper is above and to the right of the button, push the gripper
    # into the button while pushing against the wall.
    if check("the robot's gripper is above and to the right of the button and the gripper is not in contact with the wall and the gripper is not in contact with the button"):
        robot.push("gripper into button while pushing against wall")
    # To press the button, we need to slide the gripper to the right, pushing
    # against the button.
    if check("the robot's gripper is in contact with the wall and the gripper is in contact with the button"):
        robot.slide("gripper to the right, pushing against button")
```