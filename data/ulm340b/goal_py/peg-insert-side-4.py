
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Close gripper around peg
    #  4. Move peg to hole from the side
    # First, put the gripper roughly above the peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.move_gripper("above the hole")

# peg-unstack-side: unstack the peg from the block
def peg_unstack_side(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Pull the peg out from the block
    # First, put the gripper roughly above the peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.move_gripper("above the block")

# peg-insert-topdown: grab the peg and insert it into the hole from