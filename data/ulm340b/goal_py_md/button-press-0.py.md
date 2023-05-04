

The difference between `button-press` and `button-press-topdown` is that `button-press` needs to approach the button from the front, as opposed to above.

To do this, the robot will need to line up its gripper with the button as viewed from the side.
This means moving its gripper `horizontally aligned with button`.

The code will look very similar to `button-press-topdown`, except for the name and the directions in which the gripper must be lined up.

The code might look like this (not checking the robot's gripper being closed):

```
# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push the button from the front
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button")
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("near the button")
```

The code could also look like this:

```
# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push the button from the front
    # Line up the gripper as viewed from the side, and close it.
    # (We don't want to grab the button, just push it, so the gripper should be
    # closed already before we line it up.)
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, push the button from the front.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("in front of the button")
```

The robot will probably move its gripper down to near the button while lining it up, so closing its gripper won't accidentally grab the button.
However, you should still include the `close_gripper=True` part of the `move_gripper` call.

'''

button_press_topdown_code = '''
# button-press-topdown: push the button down from above
def button_