# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    #  1. Put gripper near the cube
    #  2. Grab the cube
    #  3. Put the cube in the target location
    # First, put the gripper near the cube.
    if check("the robot's gripper is not near the cube"):
        robot.move_gripper("near the cube")
    # If the gripper is near the cube and open, grab it.
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    # If the gripper has the cube and is near the target location, put the cube
    # down.
    if check("the robot's gripper is holding the cube and the robot's gripper is not near target location"):
        robot.move_gripper("near the target location")