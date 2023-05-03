
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move the cube sideways to the target location
    # First, put the gripper above the cube, so that we don't bump it when
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and closed, we can start moving the cube
    # to the target location.
    if check("the robot's gripper is around cube and the robot's gripper is closed"):
        robot.move_gripper("near the target location")