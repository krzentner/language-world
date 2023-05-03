
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    #  3. Overcome the short wall in the way
    # Because this is "top down", line up the robot's gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is near the button and the button is not pressed"):
        robot.move_gripper("over the walls")
    # If the button is pressed, keep pushing until it is fully pressed.
    if check("the button is pressed"):
        robot.move_gripper("near the button")