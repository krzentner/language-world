

Then continue writing the program:

```
# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Line up the robot's gripper with the wall
    #  2. Push the wall sideways until the button is revealed
    #  3. Push the button
    # If the gripper is not lined up with the wall yet, move it to the wall.
    if check("the robot's gripper is not vertically aligned with wall"):
        robot.move_gripper("vertically aligned with the wall")
    # Now that the gripper is lined up with the wall, push the wall until the
    # button is revealed.
    if check("wall is blocking access to button"):
        robot.move_gripper("slowly to the right")
    # Once the button is revealed, we can push the button.
    if check("button is not blocked by wall"):
        robot.move_gripper("above the button")
    # Push the button.
    if check("the robot's gripper is above button"):
        robot.move_gripper("near the button")
```