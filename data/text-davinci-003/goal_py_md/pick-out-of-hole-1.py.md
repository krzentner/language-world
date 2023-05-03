

# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Line up the gripper with the top of the peg
    #  2. Drop the gripper around the peg
    #  3. Pull the peg out of the hole
    #  4. Move the peg to the target location
    # First, we need to line up the gripper as viewed from above with the top of the peg.
    if check("the robot's gripper is not vertically aligned with the top of the peg"):
        robot.move_gripper("vertically aligned with the top of the peg")
    # As long as the gripper is lined up with the top of the peg, closing it
    # should line it up well enough to trap the peg.
    # Drop the gripper around the peg and make sure we keep control of the peg by opening it.
    if check("the robot's gripper is vertically aligned with the top of the peg"):
        robot.move_gripper("to the right of the top of the peg", close_gripper=True)
    # Now that the gripper has the peg, we can pull it out of the hole.
    if check("the robot's gripper is around the peg but the peg is still in the hole"):
        robot.move_gripper("upward aligned with the peg")
    # Once the peg is out of the hole, move it to the target location.
    if check("the peg is not in the hole"):
        robot.move_gripper("above the target location")