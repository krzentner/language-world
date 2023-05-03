# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button
    # The button is a simple task. We just need to put the gripper above the
    # button and push down.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("near the button")