
    # Steps:
    #  1. Put gripper left of door lock
    #  2. Turn door lock
    # First put the gripper to the left of the door lock.
    if check("the robot's gripper is not left of the door lock"):
        robot.move_gripper("left of the door lock", close_gripper=True)
    # If the door lock is in front of the robot's gripper, we should turn it.
    if check("the door lock is in front of the robot's gripper"):
        robot.move_gripper("forward aligned with the door lock")

# button-press-side: push the button sideways
def button_press_side(robot):
    # Steps:
    #  1. Put gripper left of the button
    #  2. Push the button with the gripper
    # First put the gripper to the left of the button.
    if check("the robot's gripper is not left of the button"):
        robot.move_gripper("left of the button", close_gripper=True)
    # As long as the gripper is not near the button, it should be on the left
    # side, so we can push.
    if check("the button is not in front of the robot's gripper and the robot's gripper is not near the button"):
        robot.move_gripper("horizontally aligned with the button")

# peg-insert-side-long: grab the peg and insert it into the long hole from the side
def peg_insert_side_long(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg