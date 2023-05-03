# Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around one side of cube
    #  3. Close gripper around cube
    #  4. Move cube to target location
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # Once the gripper is above the cube, drop it around one side of the cube.
    # We need to be careful to make sure the gripper is not too far to one side,
    # since we want to be able to close the gripper around the whole cube.
    if check("the robot's gripper is above the cube and the robot's gripper is not around one side of the cube"):
        robot.move_gripper("somewhat aligned with one side of the cube")
    # Once the gripper is around one side of the cube, close the gripper to
    # pick up the cube.
    if check("the robot's gripper is around one side of the cube and the robot's gripper is not closed"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Once the gripper has picked up the cube, move the cube to the target
    # location.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("near the target location")