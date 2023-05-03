# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Align the gripper with the button from the front
    #  2. Push the button
    # Since we're pushing the button from the front, we need to put the gripper
    # in the right position.
    # Move the gripper to be in front of the button, if it's not already.
    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper in front of button")
    # If the gripper is close enough to the button, try to push it.
    if check("the robot's gripper is in front of the button"):
        robot.push("button")