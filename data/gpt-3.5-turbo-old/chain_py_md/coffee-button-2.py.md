# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push the button
    # First, we need to put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the coffee button"):
        robot.put("gripper above coffee button")
    # Once the gripper is above the button, we can push it.
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.push("coffee button")