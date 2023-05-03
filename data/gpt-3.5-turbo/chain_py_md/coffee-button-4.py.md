# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Put gripper above coffee machine button
    #  2. Push down on the button
    # First, line up the gripper with the coffee machine button from above.
    if check("the robot's gripper is not vertically aligned with coffee machine button"):
        robot.put("gripper above coffee machine button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with coffee machine button"):
        robot.push("down on coffee machine button")