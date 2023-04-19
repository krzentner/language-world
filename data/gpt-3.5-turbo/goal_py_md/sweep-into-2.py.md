# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put the gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move the gripper to the starting location of the sweep
    #  4. Sweep the cube towards the target location
    #  5. Move the gripper above the target location
    # First, put the gripper above the cube
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is around the cube, lift it to the starting location of the sweep
    if check("the robot's gripper is around the cube and the gripper is not at the starting location of the sweep"):
        robot.move_gripper("at the starting location of the sweep")
    # With the gripper at the starting location, start sweeping the cube towards the target location
    if check("the robot's gripper is at the starting location of the sweep and the cube is not at the target location"):
        for i in range(5):
            robot.move_gripper("swept {}".format(i))
        robot.move_gripper("above the target location")
    # If the gripper is above the target location, release the cube
    if check("the robot's gripper is above the target location" and "the gripper is closed"):
        robot.move_gripper("above the cube", open_gripper=True)