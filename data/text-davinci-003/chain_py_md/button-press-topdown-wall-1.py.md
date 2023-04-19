

Steps:
1. Put gripper vertically above wall
2. Reach to the button with a slight angle to slide the gripper behind the wall
3. Push down on the button from the top

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    #  1. Put gripper vertically above wall
    #  2. Reach to the button with a slight angle to slide the gripper behind the wall
    #  3. Push down on the button from the top
    # First, put the gripper vertically above the wall.
    if check("the robot's gripper is not vertically aligned with the wall"):
        robot.put("gripper above wall")
    # Next, reach to the button with a slight angle to slide the gripper behind the wall.
    if check("the robot's gripper is not horizontally aligned with the button and the robot's gripper is not behind the wall"):
        robot.reach("to the button with an angle")
    # Now that the gripper is behind the wall and is horizontally alined with the button, we can push down on the button.
    if check("the robot's gripper is behind the wall and the robot's gripper is horizontally aligned with the button"):
        robot.push("down on button")
```