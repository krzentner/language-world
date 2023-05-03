
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper onto cube
    #  3. Squeeze cube with gripper
    #  4. Sweep cube in arc to target
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above the cube")
    # If the cube is not inside the gripper, drop the gripper onto the cube.
    if check("the robot's gripper is not inside cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is closed and around the cube, sweep it in an arc to the
    # target location.
    if check("the robot's gripper is inside cube and the robot's gripper is closed"):
        robot.move_gripper("above the target location")