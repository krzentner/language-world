# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push gripper straight down on the button
    
    # First, put the gripper above the button.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    
    # If the gripper is aligned with the button but not near it, move the gripper
    # down to the button to press it.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.push("gripper straight down on button")