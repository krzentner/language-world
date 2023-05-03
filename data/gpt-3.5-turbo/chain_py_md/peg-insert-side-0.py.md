# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper near the peg
    #  2. Close the gripper to pick up the peg
    #  3. Move the gripper to the hole
    #  4. Rotate the gripper to the side
    #  5. Insert the peg into the hole
    #  6. Open the gripper to release the peg

    # First, we need to put the gripper near the peg, but not too close to
    # avoid collision.
    if check("the robot's gripper is not near the peg"):
        robot.move("gripper to the side of the peg")

    # Once the gripper is near the peg, we should close the gripper to pick up
    # the peg.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around the peg")

    # Next, we should move the gripper to the hole. We should be careful not to
    # bump the peg against anything.
    if check("the robot's gripper is holding the peg and the gripper is not above the hole"):
        robot.move("gripper to the hole")

    # To insert the peg from the side, we should rotate the gripper 90 degrees
    # clockwise.
    if check("the gripper is above the hole and is not rotated to the side"):
        robot.rotate("gripper to the side")

    # Once the gripper is rotated to the side, we can insert the peg into the
    # hole.
    if check("the gripper is rotated to the side"):
        robot.push("peg into the hole")

    # Finally, we should open the gripper to release the peg.
    if check("the peg is in the hole and the gripper is holding the peg"):
        robot.open("gripper to release the peg")