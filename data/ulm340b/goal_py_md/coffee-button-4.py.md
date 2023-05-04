

and continue with the code that performs the task. Please be sure to follow
the style of the rest of the programs, including writing helpful comments.

After you have written the program, click 'Submit'.

"""


# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    """
    Steps:
    1. Line up gripper above button
    2. Move gripper around button
    3. Line up gripper as seen from front
    4. Move gripper near button
    """
    # First, line up the gripper from above, so that we don't bump the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, move it around the button.
    if check("the robot's gripper is not around the button"):
        robot.move_gripper("near the button")
    # Now that we have the gripper around the button, line it up from the front.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Finally, push down on the button to press it.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("above the button")

# window-close: slide the window closed to the right
def window_close(robot):
    """
    Steps:
    1. Put gripper left of the window handle
    2. Start pushing against the window handle to close the window
    3. Push the window closed harder
    """
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot'