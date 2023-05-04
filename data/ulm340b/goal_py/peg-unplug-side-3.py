
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and peg is not horizontally aligned with hole"):
        robot.move_gripper("above the peg")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")

# peg-insert-vertical: grab the peg and insert it into the hole from above
def peg_insert_vertical(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Close gripper around the peg
    #  4. Put the peg above the hole
    #  5. Lower the peg into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is vertically aligned with the peg and open, try to drop the
    # gripper around the peg.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is open"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # If the peg is not around the gripper, close the gripper around the peg.
    if check("the robot's gripper is forward aligned with the peg and the robot's gripper is not around the peg"):
        robot.move_gripper("above the peg", close_gripper=True)
    # Now that we've