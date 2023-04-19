
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube sideways to goal
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Once the gripper is around the cube, we need to line it up with the target
    # location.
    if check("the robot's gripper is around cube and the cube is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # Once the cube is lined up, we can push it to the target location.
    if check("the robot's gripper is around cube and the cube is horizontally aligned with the target location"):
        robot.move_gripper("near the target location")