# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Lift the peg out of the hole and move it to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg is in the hole and the gripper is not around the peg, move the gripper around the peg.
    if check("the peg is in the hole and the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Lift the peg out of the hole and move it to the target location.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("near the target location")