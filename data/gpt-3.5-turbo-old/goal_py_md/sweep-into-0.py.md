# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    # Steps:
    # 1. Put the gripper above the cube
    # 2. Drop the gripper around the cube
    # 3. Close the gripper
    # 4. Move the cube to the target location by sweeping it in
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and closed, sweep the cube into the target location.
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.move_gripper("sweep into the target location")