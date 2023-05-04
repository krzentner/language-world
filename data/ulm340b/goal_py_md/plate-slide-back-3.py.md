

Once you have written your program, please enter it into the text box below. When you are ready, hit submit.
""",
    'instruction2':
    """
Thanks! Please write another program for me. This time, I would like you to write a program to solve the `button-press-side` task.

```
# button-press-side: push the button down from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push button from side
    # First, put the robot's gripper roughly above the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is lined up above the button, we can move it to the side to
    # push the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("right of the button")
```

Please write a program to solve the `button-press-side` task by beginning with the following text:

```
# button-press-side: push the button down from the side
def button_press_side(robot):
```

When you are ready, please paste your program into the text box below.

""",
    'instruction3':
    """
Thanks! Please write one more program for me. I would like you to write a program to solve the `plate-slide-front` task.

```
# plate-slide-front: slide the plate forward into the target location
def plate_slide_front(robot):
    # Steps:
    #  1. Put gripper roughly above the plate
    #  2. Put the gripper on the plate
    #  3. Slide the plate forward into the target location
    # First, put the robot's gripper above the plate roughly.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is below the robot's gripper, we can probably push on it from
    # above.
    if check("the robot's gripper is above the plate"):
        robot.move_gripper("near the plate")
    # If the gripper is on the plate, we can push it forward into the target