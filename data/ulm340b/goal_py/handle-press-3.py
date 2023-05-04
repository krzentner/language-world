
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Push down on handle
    # If the handle is not above the gripper, move the gripper above the
    # handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the robot's gripper isn't lined up with the handle as seen from above,
    # move the gripper around the handle.
    # We can try to close the gripper to make sure we grab it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # If the handle is in front of the robot's gripper, the robot can push it
    # down.
    if check("the robot's gripper is forward aligned with handle"):
        robot.move_gripper("almost vertically aligned with handle")

# pick-place-wall: pick up the puck and hold it near the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck close to the wall
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
        robot.move_gripper("near the target location")

# handle-press-side: push down the handle from the