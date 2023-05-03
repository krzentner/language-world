# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # First, position the gripper above the coffee machine button.
    if check("the robot's gripper is not above the coffee machine button"):
        robot.move_gripper("above the coffee machine button")
    # If the gripper is not around the button, position the gripper around the
    # button and close it to ensure a good grip.
    if check("the robot's gripper is above the coffee machine button and the robot's gripper is open"):
        robot.move_gripper("around the coffee machine button", close_gripper=True)
    # Once the gripper is positioned around the button, push down on the button
    # to initiate the coffee brewing process.
    if check("the robot's gripper is around the coffee machine button"):
        robot.move_gripper("near the coffee machine button")