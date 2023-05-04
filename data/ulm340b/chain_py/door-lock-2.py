
    # Steps:
    #  1. Put gripper around the handle
    #  2. Turn the dial
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around handle"):
        robot.put("gripper around handle")
    # If the gripper is around the handle, we should be able to twist to lock
    # the door.
    if check("the robot's gripper is around handle"):
        robot.twist("the door locked")

# peg-insert-bottom: grab the peg and insert it into the hole from below
def peg_insert_bottom(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Insert the peg up into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole below it, insert it.
    if check("peg is vertically aligned with hole"):
        robot.insert("peg into hole")

# button-press-side: slide the robot's gripper towards the button to press it
def button_press_side(robot):
    # Steps:
    #  1. Put gripper to the side of the button
    #  2. Slide gripper towards the button
    # First, put the