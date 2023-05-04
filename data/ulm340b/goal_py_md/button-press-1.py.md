

(For the actual task, only the code you write inside this function is
evaluated.)

I've also included the description of the action in the function header as a
comment, to help you with step (2).

If you'd like to make sure your program can run successfully before you
evaluate the program, use the [button-press.py](button-press.py) file to
run it. If you want to make sure it is correct, compare it to the code at
the bottom of [instructions-robot.txt](instructions-robot.txt), which is
also included as the file [robot.py](robot.py).

If you're ready to evaluate the program, click the
"Continue" button below. Good luck!

"""


def button_press(robot):
    # Steps:
    #  1. Line up gripper above the button
    #  2. Drop gripper near the button, keeping the robot's gripper aligned from the side
    #  3. Push down on the button
    # Line up the robot's gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # If the robot's gripper is vertically aligned with the button as seen from the side,
    # drop the gripper near the button.
    if check("the robot's gripper is above button and the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button", close_gripper=True)
    # Now that the robot's gripper is in front of the button, we can push down on it.
    if check("the robot's gripper is above button and the robot's gripper is almost horizontally aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)


# Evaluating...

# Here's the answer we were looking for:

# ```
# # button-press: push the button from the front
# def button_press(robot):
#     # Steps:
#     #  1. Line up gripper above the button
#     #  2. Drop gripper near the button, keeping the robot's gripper aligned from the side
#     #  3. Push down on the button
#     # Line up the robot's gripper above the button.
#     if check("the robot's grip