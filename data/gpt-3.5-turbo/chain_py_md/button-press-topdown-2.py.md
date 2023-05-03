# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper into top of button
    #  3. Push button down
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # If the gripper is aligned with the button but not near it, move the gripper
    # down to the button to press it.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near button"):
        robot.push("the gripper into the button")
    # If the gripper is near the button, we've probably pressed the button and can release the gripper.
    if check("the robot's gripper is near the button"):
        robot.release("the gripper")
        robot.move("the gripper up")