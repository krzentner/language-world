
    # Steps:
    #  1. Put gripper near door lock
    #  2. Rotate the dial in the direction to unlock
    # Just grab the door lock and turn it.
    if check("the robot's gripper is not near door lock"):
        robot.hold("door lock")
    # If we're holding the lock, just turn it.
    if check("the robot's gripper is near door lock"):
        robot.turn("lock in the direction to unlock")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper roughly in front of the button
    #  2. Slide the button in the direction to press
    # Just push the button sideways until it's pressed.
    if check("the robot's gripper is not roughly in front of the button"):
        robot.hold("near button")
    # If the gripper is near the button, we can start pushing.
    if check("the robot's gripper is near button"):
        robot.slide("button in the direction to press")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg down into the hole
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
   