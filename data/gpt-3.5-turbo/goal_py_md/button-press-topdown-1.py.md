# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put the gripper center over the button
    #  2. Push the gripper down on the button
    # First, put the gripper center over the button.
    if check("the robot's gripper is not center over the button"):
        robot.move_gripper("center over the button")
    # Once the gripper is center over the button, we can push the gripper down on the button.
    if check("the robot's gripper is over the button"):
        robot.move_gripper("above the button", close_gripper=True)