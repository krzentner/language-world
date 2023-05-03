# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper near peg from the side
    #  2. Grab the peg
    #  3. Align the gripper with the hole from the side
    #  4. Move the gripper and insert the peg into the hole
    # First, put the gripper near the peg from the side.
    if check("the robot's gripper is not near the peg from the side"):
        robot.move("gripper near peg from the side")
    # Once the gripper is near the peg, we should be able to grab the peg.
    if check("the robot's gripper is near the peg from the side and the robot's gripper is not closed around the peg"):
        robot.grab("the peg from the side")
    # With the peg held, move the gripper to line up with the hole from the side.
    if check("the robot's gripper is closed around the peg and the robot's gripper is not aligned with the hole from the side"):
        robot.move("gripper to align with hole from the side")
    # Once aligned, move the gripper forward to insert the peg into the hole.
    if check("the robot's gripper is aligned with the hole from the side and the peg is not inserted into the hole"):
        robot.move("gripper forward to insert the peg into the hole")