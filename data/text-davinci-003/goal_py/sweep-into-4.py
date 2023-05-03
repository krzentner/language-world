
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Sweep the cube to target
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.move_gripper("around the cube")
    # If the gripper is around the cube, we can sweep it to the target location.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("near the target location")