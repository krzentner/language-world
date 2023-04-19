
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Move cube sideways to goal
    # First, put the gripper roughly above the cube, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Once the gripper is around the cube, we can just move it sideways to the
    # target location.
    if check("the robot's gripper is around cube"):
        robot.move_gripper("near the target location")