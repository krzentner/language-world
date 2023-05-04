
    # Steps:
    #  1. Put gripper above the peg
    #  2. Put gripper around the peg
    #  3. Close gripper around peg
    #  4. Pick up the peg
    #  5. Put the peg at the goal
    # If the gripper is not aligned with the peg from the top down, move the
    # gripper to be vertically aligned with the peg.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    # If the gripper is not around the peg, put the gripper around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and open, we can try to grab it by closing
    # the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # We closed the gripper, and the peg is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the peg up and out of the hole.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around peg and the robot's gripper is closed and peg is below the robot's gripper"):
        robot.pick("peg out of hole")
    # Now that we have the peg in our gripper, move the peg to the goal.
    if check("the robot's gripper is around peg and the robot's gripper is closed and the robot's gripper is not near reach goal"):
        robot.place("the peg at the goal")

# pick-insert-into-hole: pick up the peg and insert it into the hole
def pick_insert_into_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Put gripper around the peg
    #  3. Close gripper around peg
    #  4. Move the peg to above the hole
    #  5. Lower the peg into the hole
    # If the gripper