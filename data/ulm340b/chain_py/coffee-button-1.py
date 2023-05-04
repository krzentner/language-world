
    # Steps:
    #  1. Put gripper roughly above the button
    #  2. Line up the gripper above the button
    #  3. Push the button
    # If the gripper is not above the button, put it above the button.
    if check("the robot's gripper is not above coffee button"):
        robot.put("gripper above coffee button")
    # If the gripper is above the button, but not lined up, line it up.
    if check("the robot's gripper is above coffee button"):
        robot.align("gripper above coffee button")
    # If the robot's gripper is lined up above the button, press the button.
    if check("the robot's gripper is above coffee button and the robot's gripper is vertically aligned with coffee button"):
        robot.push("coffee button")

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
    # If the door is aligned with the gripper as seen from in front, we can
    # push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# block-insert-side: put the large block in the large hole sideways
def block_insert_side(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Line up the gripper with the block
    #  3. Line up the block with the hole
    #  4. Slide the block into the hole
    # First, put the gripper above the block.
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above the block")
    # If the block becomes left of the gripper, go back to