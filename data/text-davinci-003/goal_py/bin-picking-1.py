
    # Steps:
    #  1. Put gripper near cube
    #  2. Grab cube with gripper
    #  3. Move cube to target bin
    # We need to put the gripper near the cube, so it can grab it.
    if check("the robot's gripper is not near cube"):
        robot.move_gripper("near cube")
    # Once the gripper is close to the cube, we can try to grab it by closing the
    # gripper.
    # Make sure to close the gripper firmly so it grabs the cube tightly.
    if check("the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is closed around the cube, move it to the target bin.
    # Since the robot's gripper is much faster than the cube, make sure to move
    # the cube at a constant speed.
    if check("the robot's gripper is closed"):
        robot.move_gripper("near the target bin")