
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab the cube with the gripper
    #  3. Slide the cube to the goal
    # If the cube isn't below the gripper as seen from above, move the gripper
    # above the cube.
    if check("the robot's gripper is not above cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put("the gripper above the cube")
    # If the gripper is aligned with the cube but not near it, move the gripper
    # down to the cube to grab it.
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near cube"):
        robot.grab("cube")
    # If the gripper is near the cube, we've probably grabbed it and can sweep
    # it to the target location.
    if check("the robot's gripper is near the cube"):
        robot.slide("the cube to the goal")

# pick-place-side: pick up the cube and place it to the side of the target location
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Put gripper around cube
    #  3. Grab cube with gripper
    #  4. Move cube sideways to the goal
    # First, put the gripper roughly above the cube, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
 