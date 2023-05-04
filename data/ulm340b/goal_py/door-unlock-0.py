
    # Steps:
    #  1. Put gripper in front of the door's dial
    #  2. Start turning the dial
    #  3. Turn the dial hard
    # First, put the gripper in front of the door's dial.
    if check("the robot's gripper is not in front of the door's dial"):
        robot.move_gripper("in front of the door's dial")
    # If the gripper is near the dial, start turning it.
    if check("the robot's gripper is not near the door's dial"):
        robot.move_gripper("around the door's dial")
    # If the gripper is aligned with the dial, turn hard.
    if check("the robot's gripper is forward aligned with the door's dial"):
        robot.move_gripper("around the door's dial", open_gripper=True)

# pick-place-wall: pick up the peg and hold it at the target location
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move peg to goal
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

# light-switch: flip the light switch
def light_switch(robot):
    # Steps:
    #  1. Put the gripper in front of the light switch
    #  2. Open the gripper and put