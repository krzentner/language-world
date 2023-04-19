

# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down the button

    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("near the button")