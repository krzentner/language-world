# Steps:
    #  1. Put gripper above mug handle
    #  2. Grab the handle with the gripper
    #  3. Lift the mug up
    #  4. Put gripper above target location
    #  5. Move the mug to the target location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not above the handle of the mug"):
        robot.move_gripper("above the handle of the mug")
    # Once the gripper is above the handle, close it around the handle to grab
    # the mug.
    if check("the robot's gripper is above the handle of the mug and the robot's gripper is open"):
        robot.move_gripper("around the handle of the mug", close_gripper=True)
    # Now, lift the mug up.
    if check("the robot's gripper is around the handle of the mug"):
        robot.move_gripper("above the target location")
    # Once the gripper is above the target location, move the mug to the target
    # location by lowering the gripper.
    if check("the robot's gripper is above the target location and the mug is held by the gripper"):
        robot.move_gripper("near the target location")