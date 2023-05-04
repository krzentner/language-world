
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull drawer open
    # First, put the gripper above the drawer handle, so we can grab it.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle", close_gripper=True)
    # As long as the gripper is lined up, dropping it down to grab the drawer
    # handle should line it up all the way.
    if check("the robot's gripper is near drawer handle"):
        robot.move_gripper("left of the drawer handle")

# pick: pick up the puck by closing the robot's gripper around it
def pick(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
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
        robot.move_gripper("around the puck")

# stack-topdown: lift the cube to the top of the stack from above
def stack_topdown(robot):
    # Steps:
    #  1. Lift the robot's gripper above the stack
    #  2. Put the gripper near the cube
    #  3. Close the gripper around the cube
    #  4. Line the cube up with the stack
    #  5. Drop the cube down on the stack
    # First, make sure the grip