
    # Steps:
    #  1. Put gripper roughly around the handle
    #  2. Push the handle down
    # If the gripper is not near the handle, move it to the handle.
    # We don't need to be careful about the direction, since the handle is large
    # and we're just pushing it.
    if check("the robot's gripper is not near the handle"):
        robot.grab("handle")
    # If the handle is aligned with the gripper as seen from in front, we can
    # push the handle down.
    if check("the robot's gripper is forward aligned with handle"):
        robot.push("the handle down")

# button-press-side: push the button down from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper roughly to the side of the button
    #  2. Push the button down from the side
    # If the gripper is not near the button, move it to the button.
    # We don't need to be careful about the direction, since the button is large
    # and we're just pushing it.
    if check("the robot's gripper is not near the button"):
        robot.grab("button")
    # If the button is aligned with the gripper as seen from the side, we can
    # push the button down.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("the button down")

# drawer-toggle: open or close the drawer
def drawer_toggle(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed or pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it.
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    # If the drawer is aligned with the gripper as seen from