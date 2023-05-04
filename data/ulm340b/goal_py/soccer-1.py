
    # Steps:
    #  1. Put gripper around soccer ball
    #  2. Push soccer ball to the target location
    # As long as the gripper is in front of the soccer ball, push the soccer
    # ball to the target location.
    if check("the robot's gripper is in front of soccer ball"):
        robot.move_gripper("near soccer ball")

# peg-unstack: grab the top peg and unstack it
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above the top peg
    #  2. Grab the top peg
    #  3. Slide the top peg straight up
    # Line the robot's gripper up with the top peg.
    if check("the robot's gripper is not above the top peg"):
        robot.move_gripper("above the top peg")
    # As long as the top peg is roughly below the gripper, move the gripper
    # down onto the peg.
    # Because the peg is long, check if the gripper is aligned with it from the
    # front instead of around it.
    if check("the top peg is below the robot's gripper"):
        robot.move_gripper("near the top peg")
    # As long as the gripper is above the top peg, just lift it straight up.
    if check("the robot's gripper is above the top peg"):
        robot.move_gripper("above the top peg", close_gripper=True)

# pick-place-wall: grab the puck and hold it in front of the target location on a table
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck towards the target location
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot'