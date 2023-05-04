

Your function should do the following:

1. If the button is not directly below the robot's gripper, move the robot's gripper above the button.
1. If the button is below the robot's gripper, push the button downward by moving the gripper down.

You can test your program on the robot. You should see it perform the task you described.
"""
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push down on button
    # First, put the gripper directly above the button.
    if check("the button is not vertically aligned with the robot's gripper"):
        robot.place("gripper above the button")
    # As long as the button is below the gripper, we can keep pressing it.
    # The button is too small to grab and move like a puck, so we'll just press
    # it.
    if check("the button is below the robot's gripper"):
        robot.push("button down")

# button-press-side: push the button in sideways
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push down on button
    # First, put the gripper above the button.
    if check("the button is not vertically aligned with the robot's gripper"):
        robot.move("gripper above button")
    # As long as the button is vertically aligned with the robot's gripper, we
    # can keep pressing it.
    # The button is too small to grab and move like a puck, so we'll just press
    # it.
    if check("the button is vertically aligned with the robot's gripper"):
        robot.push("button down")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push down on button
    # First, put the gripper directly above the button.
    if check("the button is not vertically aligned with the robot's gripper"):
        robot.place("gripper above the button")
    # As long as the button is below