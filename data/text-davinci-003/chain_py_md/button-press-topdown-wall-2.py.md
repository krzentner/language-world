

Then write the code:

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Put gripper above wall
    #  2. Move gripper horizontally to line up with button 
    #  3. Push down on the button 
    # First, put the gripper above the wall.
    if check("the robot's gripper is not above wall"):
        robot.put("gripper above wall")
    # As long as the gripper is above the wall, we can move it left and right to
    # get it lined up with the button.
    if check("the robot's gripper is above wall and the robot's gripper is not horizontally aligned with the button"):
        robot.align("gripper to button")
    # Now that the gripper is lined up, try to push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")
```