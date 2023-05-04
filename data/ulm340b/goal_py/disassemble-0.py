
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Drop gripper around the wrench
    #  3. Close gripper around the wrench
    #  4. Move gripper left to pull the wrench off the peg
    # First, put the gripper roughly above the wrench, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # As long as the gripper is above the wrench, putting it around the wrench
    # should work.
    if check("the robot's gripper is above the wrench"):
        robot.move_gripper("above the wrench", close_gripper=True)
    # If the robot's gripper is near the wrench and open, maybe we can grab it
    # by closing the gripper.
    if check("the robot's gripper is near the wrench and the robot's gripper is closed"):
        robot.move_gripper("in front of the wrench")

# button-press-side: push the button in from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button from the side
    # This is a "side" button-pressing, so we just need to line up the gripper
    # from the side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.move_gripper("horizontally aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push the button from the side.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("left of the button")

# peg-insert-vertical: grab the peg and insert it into the hole from above
def peg_insert_vertical(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Close gripper around the peg
    # 