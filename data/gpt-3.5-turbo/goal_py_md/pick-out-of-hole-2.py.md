# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Lower the gripper into the hole
    #  3. Close gripper around peg
    #  4. Lift gripper out of the hole
    #  5. Move gripper to target location
    # First, put the gripper above the hole.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.move_gripper("vertically aligned with the hole")
    # Lower the gripper into the hole to grab the peg.
    if check("the robot's gripper is above the hole and the robot's gripper is not near the peg"):
        robot.move_gripper("inside the hole", close_gripper=True)
    # Lift the gripper out of the hole while holding onto the peg.
    if check("the robot's gripper is near the peg and the robot's gripper is holding the peg"):
        robot.move_gripper("vertically aligned with the target location")
    # Move the gripper to the target location.
    if check("the robot's gripper is vertically aligned with the target location and holding the peg"):
        robot.move_gripper("above the target location")