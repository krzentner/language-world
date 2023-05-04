
    # Steps:
    #  1. Put gripper around wrench
    #  2. Pull wrench off peg
    # First, put the gripper around the wrench.
    if check("the robot's gripper is not near wrench"):
        robot.grab("wrench")
    # If the robot's gripper is near the wrench and the wrench is vertically
    # aligned with the robot's gripper, we can pull the wrench off the peg.
    if check("the robot's gripper is near wrench and the robot's gripper is vertically aligned with wrench"):
        robot.lift("wrench up")

# peg-insert-topdown: grab the peg and insert it into the hole
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Insert the peg into the hole
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
    # If the peg is lined up with the hole as seen from above, push down on the
    # peg to insert it.
    if check("peg is vertically aligned with hole"):
        robot.insert("peg into hole")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
 