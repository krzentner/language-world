
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop gripper around the mug handle
    #  3. Pull the mug to the target location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # If the gripper is around the handle and closed, pull the mug to the target
    # location.
    if check("the robot's gripper is around mug handle and the robot's gripper is closed"):
        robot.move_gripper("near the target location")