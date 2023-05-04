
    # Steps:
    #  1. Put gripper above cube
    #  2. Close gripper around cube
    #  3. Move cube to bin
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above cube"):
        robot.place("gripper above cube")
    # As long as the gripper is above the cube and not around the cube, move the
    # gripper down around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # As long as the gripper is around the cube, we've probably grabbed it.
    # The gripper needs to be at least roughly above the cube to pick it up.
    # When we first close the gripper, that might not be the case.
    if check("the robot's gripper is around cube and the robot's gripper is above cube"):
        robot.move("cube to bin")

# peg-insert-topdown: insert the peg into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Close gripper around peg
    #  3. Line peg up with hole
    #  4. Insert peg into hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above peg"):
        robot.place("gripper above peg")
    # As long as the gripper is above the peg and not around the peg, move the
    # gripper down around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # If the gripper is around the peg, we've probably grabbed it.
    # As long as the gripper is around the peg but not lined up with the hole,
    # line it up.
    if check("the robot's gripper is around peg and the peg is not above hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the