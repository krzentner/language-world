 

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push the button down
    #  3. Release the button
    # First, put the gripper roughly above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # If the gripper is aligned above the button, start pushing the button down.
    if check("the robot's gripper is above the button"):
        robot.push("gripper into button")
    # If the button is pressed, release the button.
    if check("the robot's gripper is below the button"):
        robot.release("the button")