

# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Lower gripper onto the button
    #  3. Push the button
    # We need to put the gripper above the button before pushing it, so that we don't accidentally off-center it.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    # If the gripper is not downward aligned with the button, lower the gripper
    # onto the button.
    if check("the robot's gripper is not downward aligned with the button"):
        robot.put("gripper onto button")
    # If the gripper is around the button, we should be able to push it.
    if check("the robot's gripper is downward aligned with the button"):
        robot.push("down on button")