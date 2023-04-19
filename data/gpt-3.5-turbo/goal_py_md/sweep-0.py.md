# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with the gripper
    #  3. Move sideways while holding the cube
    #  4. Move the cube to the target location
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube, move the cube sideways.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("left of the cube")
    # If the gripper, and therefore the cube, is left of the target location,
    # move it to the target location.
    if check("the robot's gripper is left of the target location"):
        robot.move_gripper("near the target location")