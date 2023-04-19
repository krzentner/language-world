# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
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
    # If the gripper is near the cube and closed, grab the cube and lift it
    # slightly.
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.move_gripper("above the cube", lift_cube=True)
    # If the cube is lifted and the gripper is left of the target, move the
    # gripper to above the target and lower the cube onto the target.
    if check("the robot's gripper has lifted the cube and the robot's gripper is left of the target"):
        robot.move_gripper("above the target location", lower_cube=True)
    # If the cube and gripper are above the target, move the gripper sideways
    # to deposit the cube at the target location.
    if check("the robot's gripper has lowered the cube onto the target"):
        robot.move_gripper("sideways to the target location")