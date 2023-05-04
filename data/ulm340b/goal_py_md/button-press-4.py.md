

When ready, save and close.

```
# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the button forward
    # First, put the gripper roughly left of the button, so that we don't bump it while trying to push it.
    if check("the robot's gripper is not left of button"):
        robot.move_gripper("left of button")
    # Line up the robot's gripper as seen from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with button")
    # If the robot's gripper is left of the button, push it to the side.
    if check("the robot's gripper is left of button"):
        robot.move_gripper("near the button")
```
"""
# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the button forward
    # First, put the gripper roughly left of the button, so that we don't bump it while trying to push it.
    if check("the robot's gripper is not left of button"):
        robot.move_gripper("left of button")
    # Line up the robot's gripper as seen from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with button")
    # If the robot's gripper is left of the button, push it to the side.
    if check("the robot's gripper is left of button"):
        robot.move_gripper("near the button")


###############################################################
##
##    Congratulations! This completes the coding section of the evaluation.
##    After a short break, we will ask you to explain the reasoning behind your code.
##
###############################################################
print("Congratulations! This completes the coding portion of the evaluation.")
print("After a short break, we will ask you to explain the reasoning behind your code.")
input("Hit Enter to begin the second portion of the evaluation: ")


"""