

The task is to grab the peg and insert it into the hole from the side.

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper at the side of the peg
    #  2. Grab the peg
    #  3. Rotate the peg
    #  4. Insert the peg into the hole
    # First, move the gripper to the side of the peg.
    if check("the robot's gripper is not at the side of the peg"):
        robot.put("gripper at the side of the peg")
    # We should then grab the peg at the side.
    if check("the robot's gripper is at the side of the peg and the robot's gripper is not around the peg"):
        robot.grab("peg at the side")
    # Next, rotate the peg with the gripper.
    if check("the robot's gripper is around the peg"):
        robot.rotate("peg clockwise")
    # Lastly, insert the rotated peg into the hole.
    if check("the rotated peg is lined up with the hole"):
        robot.push("peg into the hole")