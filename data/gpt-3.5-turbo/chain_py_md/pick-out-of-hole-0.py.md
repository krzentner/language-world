# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper around the hole with the gripper's tips inside the hole to get a grip on the peg
    #  2. Lift the peg out of the hole
    #  3. Move the peg to the target location
    # First, put the gripper around the hole, so that we can get a grip on the peg.
    if check("the robot's gripper is not around the hole and the robot's gripper is open"):
        robot.put("gripper around the hole with the gripper's tips inside the hole")
    # Once the gripper is around the hole with the tips inside, we can close the
    # gripper to grip the peg.
    if check("the robot's gripper is around the hole with the gripper's tips inside the hole and the robot's gripper is open"):
        robot.close("gripper around the hole with the gripper's tips inside the hole")
    # Once we have a grip on the peg, we can lift it out of the hole.
    if check("the robot's gripper is around the peg"):
        robot.pull("peg out of hole")
    # If the peg is out of the hole, move it to the target location.
    if check("the peg is not in the hole"):
        robot.place("peg at target location")