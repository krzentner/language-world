# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper in front of the button
    #  2. Move gripper around button
    #  3. Press down on the button
    # First, put the gripper in front of the button.
    if check("the robot's gripper is not in front of button"):
        robot.move("gripper to front of button")
    # Once the gripper is in front of the button, bring it around the button to
    # hold it.
    if check("the robot's gripper is in front of the button and the robot's gripper is not around button"):
        robot.drop("gripper around button")
    # Finally, push down on the button.
    if check("the robot's gripper is around button"):
        robot.push("down on button")