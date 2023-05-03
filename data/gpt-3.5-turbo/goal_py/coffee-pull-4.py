# Steps:
    #  1. Put gripper around mug handle
    #  2. Lift mug off the table
    #  3. Move mug to the target location
    # First, put the gripper around the handle of the mug.
    if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Once the gripper is around the handle, lift the mug off the table.
    if check("the robot's gripper is around the mug handle and the mug is on the table"):
        robot.move_gripper("above the mug")
    # Move the mug to the target location.
    if check("the robot's gripper is above the mug and not near the target location"):
        robot.move_gripper("near the target location")