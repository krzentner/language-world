# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Slide the gripper into the hole
    #  3. Close gripper around the peg
    #  4. Pull gripper out of the hole until it is ready to move to the target location
    #  5. Move the gripper to the target location
    # First, put the gripper above the hole.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.move_gripper("vertically aligned with the hole")
    # Once the gripper is above the hole, slide it into the hole.
    if check("the robot's gripper is vertically aligned with the hole and the robot's gripper is not in the hole"):
        robot.move_gripper("into the hole", close_gripper=False)
    # Once the gripper is in the hole, close it around the peg.
    if check("the robot's gripper is in the hole and the peg is between the gripper fingers"):
        robot.move_gripper("near the hole", close_gripper=True)
    # Once the gripper has closed around the peg, pull it out of the hole.
    if check("the peg is grasped securely by the gripper and the gripper is partially out of the hole"):
        robot.move_gripper("partially out of the hole")
    # Finally, move the gripper to the target location while holding the peg.
    if check("the gripper is at least partially out of the hole and not near the target location"):
        robot.move_gripper("near the target location", close_gripper=True)