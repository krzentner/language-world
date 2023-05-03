# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button
    # First, position the gripper above the button on the coffee machine.
    if check("the robot's gripper is not vertically aligned with the coffee button"):
        robot.put("gripper above coffee button")
    # Once the gripper is lined up with the button, push down on it.
    if check("the robot's gripper is vertically aligned with the coffee button"):
        robot.push("down on coffee button")