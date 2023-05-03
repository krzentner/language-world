

The task to perform is: Push the button down from above.

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push gripper into top of button
    #  3. Push button down
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # If the robot's gripper is above the button, but it's not vertically
    # aligned, we should align the gripper with the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is lined up with the button, we can push the button by
    # pushing the gripper into the top of it.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near button"):
        robot.move_gripper("near the button", close_gripper=True)
    # If the button is now held by the gripper, we can push it down the rest of
    # the way.
    if check("the robot's gripper is near the button and the button is below the robot's gripper"):
        robot.move_gripper("downward")