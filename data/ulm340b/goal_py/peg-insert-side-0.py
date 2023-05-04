
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move peg around the goal
    #  5. Push peg into the goal
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above peg"):
        robot.move_gripper("above peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near peg", close_gripper=True)
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is around peg"):
        robot.move_gripper("above the target location")
    # If the gripper is near the target location, push the peg in!
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("vertically aligned with the target location")

# peg-insert-side-only: grab the peg and insert it into the hole from the side
def peg_insert_side_only(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move peg around the goal
    #  5. Push peg into the goal
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above peg"):
        robot.move_gripper("above peg", close_gripper=True)
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg"):
        robot.move_gripper("near peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper