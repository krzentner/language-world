
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move gripper up to lift peg
    #  5. Move peg to goal
    # First, put the gripper roughly above the peg, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg and the gripper is closed, move the
    # gripper up.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.move_gripper("near the target location")

# pick-horizontal: pick up the puck horizontally and hold it at the target location
def pick_horizontal(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Move gripper to one side of puck
    #  3. Slide gripper to edge of puck
    #  4. Close gripper
    #  5. Lift puck and move to goal
    # First, put the gripper roughly above the puck, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't horizontally aligned with the puck, put it
    # horizontally aligned with the puck.
    if check("the robot's gripper is not horizontally aligned with the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck, we can probably slide it to the target
    # location.
    if check("the robot's gripper is above the puck"):
        robot.move_gripper("above the target location")