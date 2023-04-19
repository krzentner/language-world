# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Move the gripper up out of the hole
    #  4. Move the gripper to the target location
    # First, put the gripper above the peg using the same process as in peg_insert_side.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the gripper is not around the peg, grab the peg.
    if check("the peg is not in the robot's gripper"):
        robot.grab("the peg")
    # Move the gripper up out of the hole now that we have the peg.
    if check("the robot's gripper is still in the hole"):
        robot.lift("gripper out of hole")
    # Move the gripper to the target location.
    if check("the robot's gripper is not at the target location"):
        robot.move("gripper to goal")