

then copy the code from the `button-press-topdown` example, paste it after
the `plate-slide-back-side` example, and modify it to achieve your goal.

When you are finished writing the program, run:

```
python3 submit.py
```

to submit it to the grader. You can use `submit.py` multiple times, but after
each time you should modify your program to fix any bugs. The grader will
not tell you what the bugs are; it will be like a real programming
assignment!

There will be multiple rounds of this assignment. In each round, you will be
able to submit programs for one more task. In later tasks, the robot will be
able to do a wider range of actions, because we will provide more example
programs, and because the robot itself will have more features.

Good luck!
"""

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")


# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able
    # to grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle