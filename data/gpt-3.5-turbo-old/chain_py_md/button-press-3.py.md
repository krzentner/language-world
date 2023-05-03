# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the gripper forward to press the button
    # Because this is a "front" button press, we need to line up the gripper from the front.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move("gripper to front of button")
    # Now that the gripper is lined up, just push forward on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("forward on button")