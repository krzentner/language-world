# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Lift the peg out of the hole
    #  4. Move the gripper to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is above the peg, grab it.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Once the gripper is around the peg, lift it out of the hole.
    if check("the robot's gripper is around peg"):
        robot.move_gripper("above the hole")
    # Move the gripper to the target location.
    if check("the robot's gripper is above the hole and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")