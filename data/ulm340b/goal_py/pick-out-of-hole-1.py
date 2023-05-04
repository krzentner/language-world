
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Pull peg out of hole
    #  5. Move peg to goal
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above peg"):
        robot.move_gripper("above peg", close_gripper=True)
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.move_gripper("horizontally aligned with hole")
    # If the peg isn't above the hole, line it up with the hole
    if check("peg is not horizontally aligned with hole"):
        robot.move_gripper("above peg")
    # If the peg is aligned with the hole, pull it out.
    if check("peg is horizontally aligned with hole"):
        robot.move_gripper("above the target location")

# pick-out-of-hole-topdown: pick up the peg out of the hole and hold it at the target location, from above
def pick_out_of_hole_topdown(robot):
    # Steps:
    #  1. Line up the gripper above the peg
    #  2. Push the gripper into the peg
    #  3. Pull the peg out of the hole
    #  4. Move the peg to the target location
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper above the peg.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.move_gripper("vertically aligned with peg")
    # Now that the gripper is lined up above, close it to grab the peg.
