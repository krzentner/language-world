
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Pull the peg out from the hole
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
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, unplug it.
    if check("peg is horizontally aligned with hole"):
        robot.unplug("peg")

# shape-insert: put the shape in the hole
def shape_insert(robot):
    # Steps:
    #  1. Put gripper above the shape
    #  2. Grab the shape
    #  3. Line the shape up with the hole
    #  4. Insert the shape into the hole
    # First, put the gripper above the shape.
    if check("the robot's gripper is not vertically aligned with the shape"):
        robot.put("gripper above shape")
    # If the shape isn't near the gripper anymore, put it above the shape again.
    if check("the robot's gripper is not near shape"):
        robot.grab("shape")
    # Now that the robot has the shape, as long as the shape isn't lined up with
    # the hole, we should line it up with the hole.
    if check("