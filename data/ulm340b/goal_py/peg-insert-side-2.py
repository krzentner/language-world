
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Put gripper over the hole
    #  5. Move peg into the hole
    #  6. Open gripper
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near the peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is open and the robot's gripper is around peg"):
        robot.move_gripper("vertically aligned with the hole", close_gripper=True)
    # The peg is in the right location and the gripper is closed, so move the
    # gripper down and release the peg.
    # We'll open the gripper to help the peg fall out.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.move_gripper("in front of the hole", close_gripper=False)

# peg-insert-front: grab the peg and insert it into the hole from the front
def peg_insert_front(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move gripper behind the hole
    #  5. Move peg into the hole
    #  6. Open gripper
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If