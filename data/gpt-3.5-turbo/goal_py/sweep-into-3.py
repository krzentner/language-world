# Steps:
    #  1. Put gripper above and left of the cube
    #  2. Drop gripper around one side of the cube
    #  3. Close gripper around the cube
    #  4. Move the cube to the target location
    # First, put the gripper to the side and above the cube.
    # Because the cube is a 3D object and can be in various orientations, the gripper's
    # alignment should not be too strict.
    if check("the robot's gripper is not roughly left of and above the cube"):
        robot.move_gripper("roughly left of and above the cube")
    # If the gripper isn't around the cube yet, drop it around one side of the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Once the gripper is around the cube, lift it up and move it to the target location.
    if check("the robot's gripper is around the cube and the cube is not at the target location"):
        robot.move_gripper("above the target location")