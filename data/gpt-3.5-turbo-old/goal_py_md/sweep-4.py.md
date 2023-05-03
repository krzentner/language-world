# sweep: grab the cube and move it sideways to the target location
# def sweep(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Close gripper around cube
    #  3. Move the cube sideways to the target location
    # First, put the gripper above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and closed, we can move the cube
    # sideways to the target location.
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.move_gripper("left of the target location")