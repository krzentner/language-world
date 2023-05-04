
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop the gripper around the peg
    #  3. Close gripper around peg
    #  4. Pull peg out of hole
    #  5. Move peg to goal
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above peg"):
        robot.move_gripper("above peg")
    # If the gripper isn't around the peg, drop the gripper around the peg.
    if check("the robot's gripper is not around peg"):
        robot.move_gripper("near peg", close_gripper=True)
    # As long as the gripper is around the peg, we should be able to lift it out
    # by closing the gripper.
    if check("the robot's gripper is above peg"):
        robot.move_gripper("below peg")
    # When the gripper is around the peg, we can move the peg to the goal.
    if check("the robot's gripper is around peg"):
        robot.move_gripper("vertically aligned with goal")

# insert: grab the peg and insert it into the hole
def insert(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop the gripper around peg
    #  3. Close gripper around peg
    #  4. Line peg up with hole
    #  5. Push peg into hole
    # The first two steps of grabbing the peg are the same as for
    # `pick-out-of-hole`.
    if check("the robot's gripper is not above peg"):
        robot.move_gripper("above peg")
    if check("the robot's gripper is not around peg"):
        robot.move_gripper("near peg", close_gripper=True)
    # As long as the gripper is around the peg, we can line it up with the hole.
    if check("the robot's gripper is around peg"):
        robot.move_gripper("above peg")
    # When the gripper is lined up with the hole, push the peg into the hole.
    if check("peg is not horizontally aligned with hole")