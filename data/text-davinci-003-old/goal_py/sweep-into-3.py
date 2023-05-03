
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with gripper
    #  3. Move cube to target location
    # First, put the gripper in the same space as the cube.
    if check("the robot's gripper is not near the cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube but not above it, lift the gripper until
    # it's holding the cube.
    if check("the robot's gripper is near the cube and the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the robot's gripper is above cube and closed, we can move the cube.
    if check("the robot's gripper is around cubes and the robot's gripper is closed"):
        robot.move_gripper("near the target location")