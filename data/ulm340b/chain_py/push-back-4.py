
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # We can push the puck backwards.
    # As long as the puck is not below the gripper as seen from above, move the
    # gripper above the puck.
    if check("the puck is not below the robot's gripper and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# pick-place-back: pick up the puck and put it in place, but without turning
def pick_place_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
