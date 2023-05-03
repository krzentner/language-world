# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push gripper down onto the button
    #  3. Hold the button down for some time
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is not over the button, move it above the button.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not above the button"):
        robot.move_gripper("above the button", close_gripper=True)
    # If the gripper is above the button, push down on the button with the gripper.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("on top of the button")
        # Hold the button down for some time, to make sure it depresses fully.
        robot.wait(seconds=2)
        robot.move_gripper("vertically aligned with the button")