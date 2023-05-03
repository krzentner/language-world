

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move the peg to the side of the hole
    #  5. Insert the peg into the hole
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
        robot.move_gripper("at the side of the hole")
    # Once the gripper is in place, we should be able to insert the peg in the
    # hole by pushing it in with the gripper.
    if check("the robot's gripper is near side of the hole"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Once the peg is inserted in the hole, we can just open the gripper to let
    # go.
    if check("the robot's gripper is in the hole with the peg"):
        robot.move_gripper("with the peg in the hole")