# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper next to the peg
    #  2. Grab the peg
    #  3. Hold the peg above the hole and rotate it
    #  4. Move the peg into the hole
    #  5. Release the gripper to let go of the peg
    # First, move the gripper next to the peg.
    if check("the robot's gripper is not next to the peg"):
        robot.move_gripper("next to the peg")
    # Once the gripper is next to the peg, close the gripper to grab it.
    if check("the robot's gripper is next to the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Once we have the peg, hold it above the hole and rotate it to orient it
    # correctly.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("above the hole", angle=45)
    # Move the gripper into the hole to insert the peg.
    if check("the robot's gripper is above the hole"):
        robot.move_gripper("in the hole")
    # Finally, release the gripper to let go of the peg.
    if check("the robot's gripper is in the hole"):
        robot.move_gripper("above the hole", open_gripper=True)