
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push down on the handle from the side
    # Because this is "press", we just need to line up the gripper from the side.
    # Line up the gripper as viewed from the side.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.put("gripper in front of handle")
    # Now that the gripper is lined up, push the handle down.
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.push("handle down")

# bottle-open: unscrew the bottle lid
def bottle_open(robot):
    # Steps:
    #  1. Put gripper above bottle lid
    #  2. Grab lid with gripper
    #  3. Unscrew the lid
    # First, put the gripper above the bottle lid.
    if check("the robot's gripper is not vertically aligned with bottle lid"):
        robot.put("gripper above bottle lid")
    # If the gripper is above the bottle lid, grab it.
    if check("the robot's gripper is vertically aligned with bottle lid"):
        robot.grab("bottle lid")
    # If the gripper is around the bottle lid, unscrew it.
    if check("the robot's gripper is around bottle lid"):
        robot.turn("bottle lid")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # If the door is aligned with the gripper as seen from in front, we can push
    # the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# button-press: push the button down