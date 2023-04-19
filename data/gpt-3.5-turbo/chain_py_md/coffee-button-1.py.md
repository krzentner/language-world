# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    # 1. Put gripper above the button
    # 2. Push down on the button
    # First, line up the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the coffee machine button"):
        robot.put("gripper above button")
    # Now that the gripper is aligned, push down on the button.
    if check("the robot's gripper is vertically aligned with the coffee machine button"):
        robot.push("down on button on coffee machine")