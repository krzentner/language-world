

The robot needs to push the button on the coffee machine.

# coffee-button: push the button on the coffee machine
# def coffee_button(robot):
    # Steps:
    #  1. Move the gripper as viewed from above to the center of the button
    #  2. Push down on the button to push it
    # First, move the gripper above the button so that it is lined up with it.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # Close the gripper to make sure we keep control of the button while pushing.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("above the button", close_gripper=True)
    # Once the gripper is closed, push down on the button.
    if check("the robot's gripper is above the button and the robot's gripper is closed"):
        robot.move_gripper("near the button")