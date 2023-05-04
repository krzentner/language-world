
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put the gripper on the far side of the door
    #  2. Push the door closed
    # If the gripper is behind the door or near the door handle, move it to the
    # far side of the door.
    # (Don't worry about the gripper being above the door handle - we aren't
    # doing anything interesting with the door handle.)
    if check("the robot's gripper is not horizontally aligned with the door handle"):
        robot.move_gripper("horizontally aligned with the door handle")
    # If the gripper is not in front of the door, we're still putting the gripper
    # on the far side of the door.
    if check("the robot's gripper is not forward aligned with the door handle"):
        robot.move_gripper("in front of the door handle")
    # If the gripper is in front of the door handle, we're done putting the
    # gripper on the far side of the door, so we can push the door closed.
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.move_gripper("near the door handle")

# peg-unplug-side: grab the peg and pull it out of the hole to the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put the gripper in front of the peg
    #  2. Close the gripper on the peg
    #  3. Pull the peg