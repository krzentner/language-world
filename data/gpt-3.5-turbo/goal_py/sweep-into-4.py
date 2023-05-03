# Steps:
    #  1. Put gripper above the cube
    #  2. Drop gripper around the cube
    #  3. Close gripper around the cube
    #  4. Move the cube to the location by sweeping it into the gripper
    # First, put the gripper roughly above the cube, so that we don't bump into
    # it while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, move it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube and closed, move the gripper to the target
    # location by sweeping the cube into the gripper.
    if check("the robot's gripper is around the cube and closed and the robot's gripper is not near the target location"):
        robot.move_gripper("sweep into the gripper and move it to the target location")