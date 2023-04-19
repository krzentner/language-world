
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with gripper
    #  3. Move sideways to the target location
    # First, put the gripper above the cube in order to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't close to the cube, close it to the cube to capture it.
    if check("the robot's gripper is not near the cube and the gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Now, with the cube in hand, move sideways to the target location.
    if check("the robot's gripper is near the cube and the cube is below the robot's gripper"):
        robot.move_gripper("right of the target location")