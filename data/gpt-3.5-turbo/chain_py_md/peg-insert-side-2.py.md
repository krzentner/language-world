# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper near peg
    #  2. Close gripper around peg
    #  3. Move gripper towards the hole
    #  4. Tilt gripper to vertical position
    #  5. Insert peg into hole
    #  6. Tilt gripper back to horizontal position
    #  7. Release gripper to drop peg
    # First, move the gripper near the peg
    if check("the robot's gripper is not near the peg"):
        robot.move("gripper near peg")
    # Once the gripper is near the peg, we can close the gripper to grab it.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # After grabbing the peg, move the gripper towards the hole
    if check("the robot's gripper is closed and the robot's gripper is not near the hole"):
        robot.move("gripper towards hole")
    # Once near the hole, tilt the gripper to a vertical position.
    if check("the robot's gripper is near the hole and the gripper is not vertical"):
        robot.tilt("gripper to vertical position")
    # With the gripper tilted vertically, we can now insert the peg into the hole.
    if check("the robot's gripper is vertical and the peg is not inserted into the hole"):
        robot.insert("peg into the hole")
    # Now that the peg is inserted, tilt the gripper back to a horizontal position.
    if check("the robot's gripper is vertical and the peg is inserted into the hole"):
        robot.tilt("gripper to horizontal position")
    # Finally, release the gripper to drop the peg.
    if check("the robot's gripper is horizontal"):
        robot.release("gripper to drop the peg")