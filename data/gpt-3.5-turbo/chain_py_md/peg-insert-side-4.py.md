# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put the gripper next to the peg
    #  2. Drop gripper around the peg
    #  3. Close gripper around the peg
    #  4. Move the peg to the hole
    #  5. Rotate the peg so that it's vertical
    #  6. Insert the peg sideways into the hole
    # First, put the gripper next to the peg.
    if check("the robot's gripper is not next to the peg"):
        robot.move("gripper to the side of the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # We closed the gripper, and the peg is still near the gripper, so maybe we grabbed it.
    # Try to move the peg into the hole.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around the peg and the peg is near the hole"):
        robot.move("the peg to the hole")
    # If the peg is not vertical, rotate it.
    if check("the peg is not vertical"):
        robot.rotate("the peg to be vertical")
    # If the peg is vertical, insert it into the hole
    if check("the peg is vertical"):
        robot.push("the peg into the hole")