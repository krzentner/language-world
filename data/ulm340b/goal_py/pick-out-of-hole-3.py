
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop the gripper around the peg
    #  3. Close the gripper around the peg
    #  4. Lift the peg out of the hole
    #  5. Put the peg near the target location
    if check("the robot's gripper is not almost vertically aligned with the peg"):
        robot.move_gripper("almost vertically aligned with the peg", close_gripper=True)
    # If the peg is not around the gripper, put the gripper around the peg.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the peg is around the gripper, maybe we can grab the peg by closing the
    # gripper.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is lined up with the peg and closed, maybe we've grabbed it.
    if check("the robot's gripper is above the peg"):
        robot.move_gripper("near the target location")

# peg-unstack-side: grab the top peg on the side and move it to the target location
def peg_unstack_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop the gripper around the peg
    #  3. Close the gripper around the peg
    #  4. Lift the peg away from the stacked pegs
    #  5. Put the peg near the target location
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the peg is not around the gripper, put the gripper around the peg.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg")
    # If the peg is around the gripper, maybe we can grab the peg by closing the
    # gripper.
    if check("the robot's gripper is not around the peg and the robot's gripper is not closed"):
        robot.move_gripper