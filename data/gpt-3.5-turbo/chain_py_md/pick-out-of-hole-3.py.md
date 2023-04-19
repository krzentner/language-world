# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Grab the peg with the gripper
    # First, put the gripper above the hole.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.put("gripper above hole")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open and the peg is in the hole"):
        robot.close("gripper around peg")
    # We closed the gripper, and the peg is not in the hole, so we
    # haven't grabbed anything. Go back to step 1.
    if check("the robot's gripper is above hole and the robot's gripper is closed and the peg is not in the hole"):
        robot.put("gripper above hole")
    # If the gripper is closed around the peg and it's not still in the hole,
    # we must have grabbed it.
    # Try to move the peg to the goal.
    if check("the robot's gripper is closed around peg and the peg is not in the hole"):
        robot.place("peg at goal")