

# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube up
    #  4. Move the cube to the target bin
    # First, put the gripper above the cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("up", close_gripper=True)
    # If the cube is lifted, move the cube to the target bin.
    if check("the robot's gripper is near the target bin and the cube is lifted"):
        robot.move_gripper("near the target bin")
    # When the robot gets near the target bin, open the gripper to release the
    # cube.
    if check("the robot's gripper is near the target bin and the cube is in the gripper"):
        robot.move_gripper("open", close_gripper=False)