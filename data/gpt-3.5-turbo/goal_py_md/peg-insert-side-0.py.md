# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper near the peg
    #  2. Close gripper around peg
    #  3. Align the gripper as the robot approaches the side of the hole
    #  4. Move the gripper to the side of the hole
    #  5. Align the gripper with the hole
    #  6. Move the gripper into the hole
    #  7. Release the peg
    # Approach the peg from above and close the gripper around it.
    if check("the gripper is not near the peg"):
        robot.move_gripper("near the peg")
    if check("the gripper is near the peg and the gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # As the robot approaches the side of the hole, align the gripper horizontally towards it.
    if check("the gripper is gripping the peg and the robot is not aligned with the hole"):
        robot.move_gripper("vertically aligned with the hole")
        robot.move_gripper("to the right of the hole")
    # Move the gripper towards the hole.
    if check("the gripper is aligned with the hole and is right of it"):
        robot.move_gripper("horizontally aligned with the hole")
        robot.move_gripper("in front of the hole", close_gripper=True)
    # Release the peg.
    if check("the gripper is in the hole"):
        robot.move_gripper("above the hole", close_gripper=False)