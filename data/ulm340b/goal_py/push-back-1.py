
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location", close_gripper=True)

# pick-place-back: pick up the puck and hold it at the target location
def pick_place_back(robot):
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
    # If the gripper is near the puck and