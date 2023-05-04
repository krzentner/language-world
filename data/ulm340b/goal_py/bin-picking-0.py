
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to target bin
    # First, put the gripper roughly above the cube, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.move_gripper("over the target bin")

# shelf-place: place a cube on a shelf
def shelf_place(robot):
    # Steps:
    #  1. Place cube on the shelf
    #  2. Place cube in the front bin
    # If the cube is lined up above the bin, place it in the bin.
    if check("cube is vertically aligned with the front bin"):
        robot.move_gripper("near the front bin")
    # If the cube is lined up above the bin, place it in the bin.
    if check("cube is in front of the front bin"):
        robot.move_gripper("vertically aligned with the front bin")

# push-wall: slide the cube into the hole in the wall to open the gate
def push_wall(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Push gripper into top of cube
    #  3. Slide cube to the hole in the wall
    # The robot can slide the cube by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the cube isn't below the gripper as seen from above, move the gripper
    # above the cube.
    if check("the robot's grip