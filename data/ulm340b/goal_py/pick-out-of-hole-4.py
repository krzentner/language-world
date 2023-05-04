
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Pull peg out of hole
    #  5. Move peg to goal
    # First, put the gripper roughly above the peg, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is above the peg but not around it, put it around the peg.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg")
    # As long as the gripper is around the peg, we can grab it by closing the
    # gripper and then pull it out.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.move_gripper("horizontally aligned with the peg")
    # Now that we've grabbed the peg, we can move it to the goal.
    if check("the robot's gripper is around the peg and the peg is not above the target location"):
        robot.move_gripper("near the target location")

# pick-place-wall: pick up the peg in the wall and place it at the target location
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Pull peg out of wall
    #  5. Move peg to goal
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is not around the peg, drop it around the peg.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around the peg"):
        robot.move