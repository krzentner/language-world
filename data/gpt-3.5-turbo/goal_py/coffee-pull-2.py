# Steps:
    #  1. Put gripper near the handle of the mug
    #  2. Grab the handle of the mug
    #  3. Lift the mug off the surface
    #  4. Move the mug to the target location
    #  5. Place the mug down at the target location
    # First, put the gripper near the handle of the mug.
    if check("the robot's gripper is not near the mug handle"):
        robot.move_gripper("near the mug handle")
    # If the gripper is near the handle of the mug, grab the handle.
    if check("the robot's gripper is near the mug handle and the robot's gripper is open"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # If the gripper is around the handle of the mug, lift the mug off the surface.
    if check("the robot's gripper is around the mug handle and the mug is still on the surface"):
        robot.move_gripper("above the surface")
    # If the gripper is above the surface and holding the mug, move the mug to the target location.
    if check("the robot's gripper is above the surface and holding the mug and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # If the gripper is near the target location, place the mug down at that location.
    if check("the robot's gripper is near the target location and the mug is still held by the gripper"):
        robot.move_gripper("above the target location", open_gripper=True)