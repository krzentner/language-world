
    # Steps:
    #  1. Put gripper near the cube
    #  2. Grab the cube with the gripper
    #  3. Move the cube to the target bin
    # We need to put the gripper near the cube before we can grab it.
    if check("the robot's gripper is not near the cube"):
        robot.move_gripper("near the cube")
    # Once the gripper is near the cube, we can grab it by closing the gripper.
    if check("the robot's gripper is open and the robot's gripper is near the cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Once the cube is grabbed, move it to the target bin.
    if check("the robot's gripper is closed and the cube is in the robot's gripper"):
        robot.move_gripper("above the target bin")