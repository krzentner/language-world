
    # Steps:
    #  1. Put gripper above the handle
    #  2. Put gripper around the handle
    #  3. Pull up on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the handle is right of the gripper, go back to putting the gripper
    # above the handle.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("handle is not right of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.put("gripper around handle")
    # As long the gripper is still mostly around the handle and the handle is
    # still down, pull the handle up.
    if check("the robot's gripper is forward aligned with the handle and the handle is not forward aligned with the robot's gripper"):
        robot.pull("handle up")

# button-press-side: push the button with the side of the gripper
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Move the gripper to the side of the button
    #  3. Push the button sideways
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("gripper above button")
    # If the button is right of the gripper, go back to putting the gripper
    # above the button.
    # Because the button is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("button is not right of the robot's gripper and button is not forward aligned with the robot's gripper"):
        robot.align("the gripper with button")
    # As long the gripper is still mostly around the button, push the button.
    if check("the robot's gripper is forward aligned with the button and the button is not forward aligned with the robot's gripper"):
        robot.press("button sideways")

# button-