
    # Steps:
    #  1. Put gripper above the drawer handle
    #  2. Drop gripper around the drawer handle
    #  3. Pull the drawer open
    # First, put the gripper above the drawer handle.
    if check("the robot's gripper is not above drawer handle"):
        robot.place("gripper above drawer handle")
    # If the gripper is vertically aligned and open, we can probably grab the
    # drawer handle.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is open"):
        robot.drop("gripper around drawer handle")
    # As long the gripper is still mostly around the drawer handle and the
    # drawer isn't fully open, pull the drawer open.
    if check("the robot's gripper is around drawer handle and drawer handle is not to the side of the drawer"):
        robot.pull("drawer open")

# peg-insert-vertical: grab the peg and insert it vertically into the hole
def peg_insert_vertical(robot):
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
    if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole vertically, insert it.