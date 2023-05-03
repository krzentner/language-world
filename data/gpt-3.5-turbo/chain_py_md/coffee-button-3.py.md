# coffee-button: push the button on the coffee machine
# Steps:
#  1. Put gripper above the button
#  2. Push the button down
def coffee_button(robot):
    # First, put the gripper of the robot above the button on the coffee machine.
    if check("the robot's gripper is not positioned above the coffee button"):
        robot.put("gripper above coffee button")
    # Then, push the button down.
    if check("the robot's gripper is positioned above the coffee button"):
        robot.push("down on coffee button")