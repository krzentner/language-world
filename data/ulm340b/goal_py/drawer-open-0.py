
    # Steps:
    #  1. Put gripper around drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when closing the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle", close_gripper=True)
    # If the robot's gripper is aligned with the drawer handle from the side,
    # we can pull the drawer open.
    if check("the robot's gripper is left of the drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Put gripper around the button
    #  3. Push on the button
    # Move gripper to above the button
    if check("the robot's gripper is not almost vertically aligned with button"):
        robot.move_gripper("almost vertically aligned with button")
    # If the robot's gripper is vertically aligned with the button, move the
    # gripper around the button
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("around the button", close_gripper=True)
    # As long as the gripper is almost around the button, close it to grab the
    # button.
    if check("the robot's gripper is right of the button"):
        robot.move_gripper("near the button")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Drop the peg in the hole
    # First, put the gripper above the peg.
    if check("the robot