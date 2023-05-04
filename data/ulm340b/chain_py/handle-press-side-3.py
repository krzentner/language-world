
    # Steps:
    #  1. Line up the gripper with the handle from the side
    #  2. Push down on the handle
    # Because this is "side", we just need to line up the gripper from the side.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.align("gripper to handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.push("handle down")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Lower the peg into the hole
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
    # If the peg is lined up with the hole above, lower it.
    if check("peg is vertically aligned with hole"):
        robot.lower("peg into hole")

# lift-press-topdown: push down on the press down thing from above
def lift_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the press down thing