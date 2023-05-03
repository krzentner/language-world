# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Move the peg out of the hole
    #  4. Move the peg to the target location
    #  5. Hold the peg in the gripper
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # As long as the gripper is not around the peg, move it near the peg and
    # close the gripper to grab it.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg, we can move it out of the hole by lifting
    # it straight up.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("above the hole")
    # If the gripper is above the hole, move it to the target location.
    if check("the robot's gripper is above the hole and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # Finally, hold the peg in the gripper at the target location.
    if check("the robot's gripper is near the target location and the gripper is open"):
        robot.move_gripper("around the peg")