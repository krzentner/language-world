
    # Steps:
    #  1. Put gripper around the wrench
    #  2. Move the wrench over to the peg
    #  3. Lift the wrench up while turning it 180 degrees
    #  4. Put the wrench around the peg
    # Grab the wrench by putting the gripper around it.
    if check("the robot's gripper is not around wrench"):
        robot.move_gripper("around wrench")
    # Lift the wrench and move it to the side of the peg.
    if check("the robot's gripper is around wrench and wrench is almost vertically aligned with peg"):
        robot.move_gripper("vertically aligned with wrench")
    # As long as the gripper is around the wrench, lift the wrench over the peg.
    if check("the robot's gripper is around wrench and wrench is vertically aligned with peg"):
        robot.move_gripper("above wrench")
    # With the wrench above the peg, twist the gripper 180 degrees and put the
    # wrench down around the peg.
    if check("the robot's gripper is above the wrench"):
        robot.move_gripper("left of the peg")

# pick-place-wall: pick up the puck and put it at the target location
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("around the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is around the puck and the robot's gripper is closed"):