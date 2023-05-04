
    # Steps:
    #  1. Get gripper above the peg
    #  2. Drop the gripper down around the peg
    #  3. Close the gripper around the peg
    #  4. Move the peg above the hole
    #  5. Slide the peg into the hole
    # Grab the peg
    # Put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # Put the gripper around the peg.
    if check("the robot's gripper is above the peg"):
        robot.move_gripper("near the peg", close_gripper=True)
    # Now put the peg above the hole.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("above the hole")
    # Slide the peg into the hole.
    if check("the robot's gripper is around the peg and the peg is above the hole"):
        robot.move_gripper("almost above the peg")

# pick-place-wall: pick up the puck and hold it against the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck near wall
    #  5. Press puck against wall
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the wall