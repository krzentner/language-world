
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Grip the mug handle
    #  4. Pull the mug to the target location
    # If the gripper isn't already in the mug handle, move it to the mug
    # handle.
    if check("the robot's gripper is not above mug handle"):
        robot.move_gripper("above the mug handle", close_gripper=True)
    # If the gripper is already in the mug handle, just close it.
    if check("the robot's gripper is around mug handle"): 
        robot.move_gripper("near the target location")
    # If the gripper is closed around the mug handle, pull the mug to the target
    # location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location")