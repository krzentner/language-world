

and then enter the rest of the code as an indented block.
The function should have a single parameter named `robot`.

This is a good time to check if your code works properly.

"""

# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Line up the gripper with the button as viewed from above
    #  2. Push down on the button from the top
    # Because there is a wall in the way of pushing the button from the front,
    # push the button down from above.
    # Line up the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is behind button"):
        robot.put("gripper above button")
    # The button is lined up, so push it down from above.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is above button"):
        robot.push("down on button")

# This code is not shown to the participants. It is only here for testing.
def button_press_wall_alt(robot):
    # Steps:
    #  1. Line up the gripper with the button as viewed from above
    #  2. Push down on the button from the top
    # Because there is a wall in the way of pushing the button from the front,
    # push the button down from above.
    # The button is lined up, so push it down from above.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is above button"):
        robot.push("down on button")

def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

def window_open(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
