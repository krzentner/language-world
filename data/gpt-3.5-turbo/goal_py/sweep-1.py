# Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube with the gripper
    #  3. Move gripper sideways to the target location
    # First, position the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.move_gripper("vertically aligned with the cube")
    # If the gripper isn't around the cube, position it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Move the gripper sideways to the target location while holding onto the
    # cube.
    if check("the robot's gripper is around the cube"):
        robot.move_gripper("horizontally aligned with the target location")