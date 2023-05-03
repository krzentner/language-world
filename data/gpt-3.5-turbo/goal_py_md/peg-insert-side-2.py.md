# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Move gripper to the side of the hole
    #  3. Move gripper down to grab the peg
    #  4. Lift gripper up with the peg
    #  5. Move gripper to the hole
    #  6. Rotate gripper to align with the hole
    #  7. Move gripper down to insert the peg into the hole
    #  8. Lift gripper up and move away from the hole
    # First, position the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # Once the gripper is above the peg, move it to the side of the hole.
    if check("the robot's gripper is not to the side of the hole"):
        robot.move_gripper("to the side of the hole")
    # Once the gripper is at the side of the hole, move it down to grab the peg.
    if check("the robot's gripper is not grabbing the peg and the gripper is aligned with the peg"):
        robot.move_gripper("to the peg", close_gripper=True)
    # Once the gripper is holding the peg, lift it up and move it to the hole.
    if check("the gripper is holding the peg and is not aligned with the hole"):
        robot.move_gripper("near the hole")
    # Once the gripper is near the hole, rotate it to align the peg with the hole.
    if check("the gripper is near the hole and is not aligned with the hole"):
        robot.rotate_gripper()
    # Once the gripper is aligned with the hole, move it down to insert the peg.
    if check("the gripper is aligned with the hole and is not inserting the peg"):
        robot.move_gripper("into the hole")
    # Once the peg is inserted, the gripper is lifted up and moved away from the
    # hole.
    if check("the gripper is inserting the peg"):
        robot.move_gripper("near the peg", close_gripper=False)