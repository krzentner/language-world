
    # Steps:
    #  1. Put gripper roughly above the drawer handle
    #  2. Drop gripper around the drawer handle
    #  3. Pull the drawer open
    # First, put the gripper roughly above the drawer handle.
    # This doesn't have to be exact, because we'll line it up exactly in the
    # next step.
    if check("the robot's gripper is not above drawer handle"):
        robot.put("gripper above drawer handle")
    # As long as the gripper is above the drawer handle, closing it should line
    # it up.
    # If the gripper is roughly above the drawer handle, move it down.
    if check("the robot's gripper is above drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    # As long as the gripper is around the drawer handle, pull it open.
    # If the gripper is still around the drawer handle, pull the drawer open.
    if check("the robot's gripper is around drawer handle"):
        robot.pull("drawer open")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper roughly around the button
    #  2. Slide to the button from the side
    # If the gripper is not near the button, move it to the button.
    # We don't need to be careful about the direction, since the button is
    # large and we're just sliding it (unlike when pressing the button from
    # above).
    if check("the robot's gripper is not near button"):
        robot.grab("button")
    # As long as the button is forward aligned with the gripper, slide it left
    # or right, depending on where it is.
    # If the button is not forward aligned with the gripper, line it up.
    if check("button is forward aligned with the robot's gripper"):
        robot.slide("button")

# pick: pick up the puck and hold it in the air
def pick(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  