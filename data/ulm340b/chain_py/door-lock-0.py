
    # Steps:
    #  1. Put gripper above door dial
    #  2. Put gripper around door dial
    #  3. Turn the door dial
    # Put the gripper above the door dial so that we can grab it.
    if check("the robot's gripper is not vertically aligned with door dial"):
        robot.put("gripper above door dial")
    # If the gripper is lined up with the door dial as seen from above, put it
    # around the door dial so that we can turn it.
    if check("the robot's gripper is vertically aligned with door dial"):
        robot.put("gripper around door dial")
    # If the gripper is around the door dial and the dial is not locked, keep
    # turning the dial.
    if check("the robot's gripper is around door dial and door dial is not locked"):
        robot.turn("door dial")

# button-press: push the button down from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper around the button
    #  2. Press down on the button
    # We need to put the gripper around the button from the side first.
    if check("the robot's gripper is not around button"):
        robot.put("gripper around button")
    # If the gripper is lined up with the button but not near it, move the
    # gripper down to the button to press it.
    if check("the robot's gripper is around button"):
        robot.push("down on button")

# peg-insert-back: grab the peg and insert it into the hole
def peg_insert_back(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab the peg
    #  3. Line up the peg
    #  4. Insert peg into the hole
    # Because this is a "back", we'll line the peg up before grabbing it.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("