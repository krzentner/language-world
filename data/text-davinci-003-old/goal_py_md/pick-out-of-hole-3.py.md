

# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Drop gripper around the peg
    #  3. Close gripper around the peg
    #  4. Move the peg to the target location
    # First, put the gripper roughly above the hole, so that we don't miss the peg while
    # trying to grab it.
    if check("the robot's gripper is not above the hole"):
        robot.move_gripper("above the hole")
    # Once the gripper is above the hole, we can lower it down to grab the peg.
    if check("the robot's gripper is above the hole and the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg, we can move it to the target location.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("near the target location")