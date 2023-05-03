# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button
    # First, move the robot's gripper above the button on the coffee machine.
    if check("the robot's gripper is not above the coffee machine button"):
        robot.move_gripper("above the coffee machine button")
    # Once the gripper is above the button, push down on the button to start the
    # coffee machine.
    if check("the robot's gripper is above the coffee machine button"):
        robot.move_gripper("on top of the coffee machine button")