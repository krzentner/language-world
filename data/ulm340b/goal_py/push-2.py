
    # Steps:
    #  1. Put gripper right of the puck
    #  2. Slide the puck to the target location
    #  3. Push the puck against the target location
    # If the robot's gripper is not right of the puck, we should move the gripper
    # to push it.
    if check("the robot's gripper is not almost vertically aligned with the puck"):
        robot.move_gripper("almost vertically aligned with the puck")
    # If the robot's gripper is near the puck and open, maybe we can push it by
    # moving the gripper left.
    if check("the robot's gripper is forward aligned with the puck"):
        robot.move_gripper("horizontally aligned with the puck")

# pick-place-wall: pick up the puck and hold it at the target location against the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal against wall
    #  5. Move the gripper against the wall
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
    # If the robot's gripper is now above the puck, it has probably grabbed it,
    # so we can move the gripper near the target location to place it there.
    if check("the robot's gripper is above the puck"):
        robot.move_gripper("almost vertically aligned