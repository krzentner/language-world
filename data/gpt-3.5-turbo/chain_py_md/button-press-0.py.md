# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Move the gripper in front of the button
    #  2. Push down on the button
    # Because we're pressing the button from the front, we need to move the
    # gripper directly in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper to front of button")
    # Now that the gripper is in front of the button, we just need to push down
    # on the button.
    if check("the robot's gripper is in front of the button"):
        robot.push("down on button")