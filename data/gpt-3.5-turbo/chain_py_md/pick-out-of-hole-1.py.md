# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper near hole and above the peg
    #  2. Lower gripper into the hole and grab the peg
    #  3. Lift the peg out of the hole
    #  4. Move the gripper to the target location
    #  5. Release the peg at the target location
    # First, put the gripper near the hole and above the peg, so that we don't bump the hole while trying to grab the peg.
    if check("the robot's gripper is not above and near the peg in the hole"):
        robot.place("gripper above and near peg in hole")
    # If the gripper isn't around the peg, lower it into the hole and grab the peg.
    if check("the robot's gripper is above and near the peg in the hole and the robot's gripper is open"):
        robot.drop("gripper into hole and around peg")
    # If the gripper is around the peg, lift it out of the hole.
    if check("the robot's gripper is around peg in hole and the robot's gripper is near the top of the hole"):
        robot.lift("peg out of the hole")
    # If the gripper has the peg and is near the target location, move the gripper to the target.
    if check("the robot's gripper is holding peg and is not at the goal"):
        robot.place("gripper at goal")
    # If the gripper is at the target location, release the peg.
    if check("the robot's gripper is at goal and the robot's gripper is holding peg"):
        robot.open("gripper at goal")