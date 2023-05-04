
    # Steps:
    #  1. Put gripper vertically above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the target bin
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper is vertically aligned with the cube, move the gripper above
    # the cube and close it.
    if check("the robot's gripper is vertically aligned with the cube"):
        robot.move_gripper("above the cube", close_gripper=True)
    # As long as the gripper is still lined up with the cube, move the cube to
    # the target bin.
    if check("the robot's gripper is near the cube"):
        robot.move_gripper("near the target bin")

# drawer-close-topdown: push the drawer closed from above
def drawer_close_topdown(robot):
    # Steps:
    #  1. Put the gripper above the drawer
    #  2. Push down on the drawer handle
    # Put the gripper above the drawer.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # If the gripper is above the drawer handle, we can just push it closed.
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.move_gripper("near the drawer handle")

# pick-place-wall: pick up the object and hold it next to the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put the gripper above the puck
    #  2. Put the gripper around the puck
    #  3. Close the gripper on the puck
    #  4. Move the puck next to the wall
    # First, put the gripper above the puck, so that we don't knock it around
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the