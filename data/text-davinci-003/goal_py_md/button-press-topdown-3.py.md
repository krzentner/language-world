

The program should include:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper roughly above button
    #  2. Align gripper with button
    #  3. Push button down
    # Put the gripper above the button, so that we don't bump it while trying to
    # press it
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # If the button is not lined up with the gripper as seen from above, move
    # the gripper to line it up.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # Once the gripper is lined up with the button, we simply push it down.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("down")

```