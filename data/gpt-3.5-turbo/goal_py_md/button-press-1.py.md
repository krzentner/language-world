# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Check if the button is low enough to push
    #  2. Move the gripper near the button from the front
    #  3. Push the button
    
    # Check if the button is low enough to push. If not, move the gripper to the
    # side and move the robot closer to the button.
    if check("the button is not low enough to push"):
        robot.move_gripper("right of the button")
        robot.move("toward the button")
    # If the button is low enough to push, move the gripper near the button from
    # the front.
    if check("the button is low enough to push and the robot's gripper is not forward aligned with the button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Push the button.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("near the button")