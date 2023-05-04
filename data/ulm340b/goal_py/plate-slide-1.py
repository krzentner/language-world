
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # The robot can slide the plate by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to slide it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it to the target location.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move_gripper("vertically aligned with the plate")

# pick-place-wall: pick up the puck and hold it at the target location in front of the wall
def pick_place_wall(robot):
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
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the grip