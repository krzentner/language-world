

The steps for this task should be:

1. Put the gripper above the wall
2. Push the wall away from the button
3. Put the gripper above the button
4. Push down on the button from the top

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Put the gripper above the wall
    #  2. Push the wall away from the button
    #  3. Put the gripper above the button
    #  4. Push down on the button from the top
    # First, put the gripper above the wall.
    if check("the robot's gripper is not above wall"):
        robot.put("gripper above wall")
    # If the gripper is above the wall, we can push the wall away from the
    # button.
    if check("the robot's gripper is above wall"):
        robot.push("wall away from button")
    # Once the wall is away from the button, move the gripper above the button.
    if check("the wall is away from the button and the robot's gripper is not above button"):
        robot.put("gripper above button")
    # If the gripper is above the button, just push down on the button.
    if check("the robot's gripper is above button"):
        robot.push("down on button")
```