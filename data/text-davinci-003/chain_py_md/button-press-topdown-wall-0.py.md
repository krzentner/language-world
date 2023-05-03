

Then add code to achieve the task:

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push gripper into the wall
    #  3. Push down on the button from the top
    # First, put the gripper above the button, but also above the wall.
    if check("the robot's gripper is not vertically aligned with button above the wall"):
        robot.put("gripper above button above the wall")
    # Once the robot's gripper is above and in front of the wall, push against
    # the wall to line up the gripper with the button.
    if check("the robot's gripper is above and forward aligned with the wall"):
        robot.push("gripper into wall")
    # Now that the gripper is in front of the button, push down on the button
    # from the top.
    if check("the robot's gripper is in front of the button"):
        robot.push("down on button")
```