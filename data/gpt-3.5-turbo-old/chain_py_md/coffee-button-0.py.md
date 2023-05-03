# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the coffee machine button
    #  2. Push down on the button
    # First, put the gripper above the coffee machine button
    if check("the robot's gripper is not above the coffee machine button"):
        robot.put("gripper above coffee machine button")
    # Once the gripper is above the coffee machine button, push down on the button
    if check("the robot's gripper is above the coffee machine button"):
        robot.push("down on button")