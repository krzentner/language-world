# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Move the gripper down to grab the peg
    #  3. Close gripper around peg
    #  4. Move peg to goal
    # First, put the gripper above the hole, so that we don't bump into anything
    # while trying to grab the peg.
    if check("the robot's gripper is not above the hole"):
        robot.place("gripper above hole")
    # If the gripper isn't around the peg and the gripper is above the hole, move
    # the gripper down around the peg.
    if check("the robot's gripper is above the hole and the robot's gripper is not around peg" ):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and the gripper is open, maybe we can grab it
    # by closing the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # We closed the gripper, and the peg is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the peg to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("peg at goal")