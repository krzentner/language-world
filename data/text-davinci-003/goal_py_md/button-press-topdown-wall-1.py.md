

Steps:
  1. Line up the gripper above the wall
  2. Move the gripper around the wall
  3. Line up the gripper as viewed from above
  4. Push down on the button from the top

```
# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # First, line up the gripper above the wall, as seen from the side.
    if check("the robot's gripper is not horizontally aligned with wall"):
        robot.move_gripper("horizontally aligned with wall")
    # Once the gripper is lined up above the wall, we should be able to reach
    # around the wall to push the button.
    if check("the robot's gripper is horizontally aligned with wall and the robot's gripper is not around wall"):
        robot.move_gripper("around the wall")
    # Once the gripper is around the wall, just line it up with the button as
    # seen from above.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Now that the gripper is lined up with the button, we can push down on the
    # button.
    if check("the robot's gripper is near the button and the robot's gripper is closed"):
        robot.move_gripper("below the button")
```