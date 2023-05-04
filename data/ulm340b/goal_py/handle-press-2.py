
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the handle from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("above the handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("around the handle")

# button-press: push the button down from the side
def button_press(robot):
    # Steps:
    #  1. Put the gripper above the button
    #  2. Push down on the button
    # If the gripper is above the button, we can push the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button", close_gripper=True)
    # Now that the gripper is above the button, push the button.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("near the button")

# pick-insert-side: grab the peg and insert it into the hole from the side
def pick_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):