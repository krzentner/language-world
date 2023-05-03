
    # Steps:
    #  1. Put gripper in front of button
    #  2. Push button
    # To press a button from the front, the gripper should be placed in front of
    # the button.
    if check("the robot's gripper is not in front of button and the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # If the button is lined up with the robot's gripper, we can push the button
    # with the robot's gripper.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("in front of the button")