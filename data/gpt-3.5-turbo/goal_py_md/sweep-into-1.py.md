# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal by sweeping it
    # First, put the gripper roughly above the cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and closed, we can sweep it to the target location.
    # First, move the gripper to the left side of the cube.
    if check("the robot's gripper is near the cube"):
        robot.move_gripper("left of the cube")
    # Sweep the cube to the target location by moving the gripper right and down.
    if check("the robot's gripper is left of the target location and the robot's gripper is near the cube"):
        robot.move_gripper("above the target location")