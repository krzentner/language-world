

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper over peg
    #  3. Close gripper around peg
    #  4. Move peg to hole, with the side of the peg facing the hole
    # First, line up the robot's gripper above the peg.
    if check("the robot's gripper is not above the peg"):
       robot.move_gripper("above the peg")
    # If the gripper isn't above the peg, we should move the gripper above it.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("over the peg")
    # Once the gripper is above the peg, we should close the gripper to grab it.
    if check("the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # Now, move the gripper towards the hole, making sure to keep the side of
    # the peg facing towards the hole.
    if check("the robot's gripper is near the peg"):
        robot.move_gripper("pointing the side of the peg towards the hole")