
    # Steps:
    #  1. Put gripper above the puck
    #  2. Push gripper into top of puck
    #  3. Slide the puck to the wall
    #  4. Push the puck against the wall
    #  5. Slide the puck around the wall
    #  6. Slide the puck to the goal
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.push("the puck against the wall")
    # If the puck is against the wall, it's probably time to slide the puck
    # around the wall.
    if check("the puck is touching the wall"):
        robot.slide("the puck around the wall")
    # If the puck is past the wall, slide it to the goal.
    if check("the puck is past the wall"):
        robot.slide("the puck to the goal")

# pick-place-wall: pick up the puck and hold it at the target location, with a small wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to the wall
    #  5. Push the puck against the wall
    #  6. Put the puck at goal
    # First, put the gripper roughly above the puck, so that we don't bump it
    # while trying to