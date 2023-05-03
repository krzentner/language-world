# Steps:
    #  1. Put gripper above the handle of the mug
    #  2. Open the gripper
    #  3. Drop the gripper around the handle of the mug
    #  4. Close the gripper to hold onto the mug handle
    #  5. Move the mug to the target location
    # First, put the gripper above the handle of the mug.
    if check("the robot's gripper is not vertically aligned with the handle of the mug"):
        robot.move_gripper("vertically aligned with the handle of the mug")
    # If the gripper is still open, drop it around the handle of the mug.
    if check("the robot's gripper is vertically aligned with the handle of the mug and the robot's gripper is open"):
        robot.move_gripper("around the handle of the mug", close_gripper=True)
    # As long as the gripper is holding onto the mug handle, move the mug to the target location.
    if check("the robot's gripper is holding onto the handle of the mug and the mug is not near the target location"):
        robot.move_gripper("near the target location")