
    # Steps:
    #  1. Put gripper above coffee button
    #  2. Push down on coffee button from the top
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not above coffee button"):
        robot.move_gripper("vertically aligned with the coffee button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is above coffee button"):
        robot.move_gripper("near the coffee button")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is aligned with the gripper as seen from in front, we can push
    # the door closed.
    if check("the robot's gripper is forward aligned with the door handle"):
        robot.move_gripper("vertically aligned with the door handle")

# pick: pick up the peg from above
def pick(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Close gripper around peg
    # First, put the gripper roughly above the peg, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is near the peg and open, maybe we can grab it by closing
    #