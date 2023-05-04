
    # Steps:
    #  1. Put gripper left of the door lock
    #  2. Turn the lock
    # First, put the gripper mostly left of the door lock.
    if check("the robot's gripper is not almost left of door lock"):
        robot.put("gripper left of door lock")
    # As long the gripper is mostly left of the door lock, turn the door lock.
    if check("the robot's gripper is almost left of door lock and the door lock is not vertical"):
        robot.turn("door lock")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper left of the button
    #  2. Push the button from the side
    # Because this is "side", we just need to line up the gripper left of the
    # button.
    # Put the gripper left of the button.
    if check("the robot's gripper is not left of button"):
        robot.put("gripper left of button")
    # Now that the gripper is left of the button, just push the button.
    if check("the robot's gripper is left of button"):
        robot.push("button")

# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper left of the dial
    #  2. Turn the dial
    # First, put the gripper mostly left of the dial.
    if check("the robot's gripper is not almost left of dial"):
        robot.put("gripper left of dial")
    # As long the gripper is mostly left of the dial, turn the dial.
    if check("the robot's gripper is almost left of dial and the dial is not horizontal"):
        robot.turn("dial")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    #