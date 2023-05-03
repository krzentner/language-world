# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move to hole
    #  5. Turn gripper to side
    #  6. Move gripper to the desired side of the hole
    #  7. Insert peg into hole
    # First, put the gripper above the peg, being careful not to knock it over.
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    # Once above the peg, lower the gripper and try to grab the peg.
    if check("the robot's gripper is above peg and the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    # If the gripper is around the peg, try to grip it firmly.
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # We should now have the peg, so move the gripper to the hole.
    # Remember the robot's gripper cannot move sideways, so it must go straight
    # to the hole.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.reach("hole")
    # Now that the gripper is over the hole, turn it so that it is parallel to
    # the hole.
    if check("the robot's gripper is over hole"):
        robot.turn("gripper parallel to hole")
    # Move the gripper to the desired side of the hole.
    if check("the robot's gripper is parallel to hole"):
        robot.move("gripper to side of hole")
    # Insert the peg into the hole.
    # We can grip from above and push down directly because the hole is large.
    if check("the robot's gripper is aligned with the hole"):
        robot.push("peg into hole")