
    # Steps:
    #  1. Put gripper above button
    #  2. Drop gripper around button
    #  3. Push button down
    #  4. Push button harder
    # First, put the gripper above the button.
    # We want to make sure the gripper is not blocking the button, so make sure
    # we're lined up from the side instead of above it.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with button")
    # If the button becomes right of the gripper, go back to putting the gripper
    # above the button.
    if check("button is right of the robot's gripper and the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # As long as the gripper is still around the button and the button is not
    # pressed, push the button down.
    if check("button is pressed"):
        robot.move_gripper("above the button")
    # If the button starts to become unpressed, push harder.
    if check("the robot's gripper is around button and the button is not pressed"):
        robot.move_gripper("forward aligned with the button")