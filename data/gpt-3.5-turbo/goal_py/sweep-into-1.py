# Steps:
    #  1. Move the gripper over the cube
    #  2. Close the gripper around the cube
    #  3. Lift the cube off the surface
    #  4. Move the gripper to the target location
    #  5. Lower the cube onto the surface
    # Move the gripper roughly over the cube.
    if check("the robot's gripper is not near the cube"):
        robot.move_gripper("near the cube")
    # If the gripper isn't around the cube yet, move it around the cube and
    # close the gripper.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Now that the gripper is around the cube, lift the cube off the surface.
    if check("the robot's gripper is closed and the cube is still on the surface"):
        robot.move_gripper("above the target location")
    # Move the gripper to the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location", close_gripper=True)
    # Lower the cube onto the surface at the target location.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("near the target location", close_gripper=False)