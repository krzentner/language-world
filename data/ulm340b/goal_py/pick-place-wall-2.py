
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("around the puck")
    # If the gripper is around the puck and closed, move the gripper towards
    # the target location.
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.move_gripper("near the target location", close_gripper=True)

# pick-place-topdown: pick up the puck from directly above, then hold it at the target location
def pick_place_topdown(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # We need to put the gripper above the puck before we can grab it, because of
    # the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("around the puck")
    # If the gripper is around the puck and closed, move the gripper towards
    # the target location.
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.move_gripper("near the target location", close_gripper=True)

# peg-unstack: remove the red peg from the green peg