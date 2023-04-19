# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Line up the gripper with the button from the front
    #  2. Push down on the button
    # We need to line up the gripper with the button from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper with button horizontally")
    # Once the gripper is aligned with the button from the front, we can push
    # down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")