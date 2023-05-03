# Steps:
    #  1. Put gripper above the handle of the mug
    #  2. Drop gripper around the handle of the mug
    #  3. Close gripper around the handle of the mug
    #  4. Move mug to the target location by sliding it
    # First, put the gripper above the mug handle, so that we can easily grab it.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.move_gripper("vertically aligned with the mug handle")
    # If the gripper is lined up, drop it around the handle of the mug by moving
    # the gripper down.
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is not around the mug handle"):
        robot.move_gripper("around the mug handle")
    # Close the gripper around the mug handle once the gripper is around the
    # handle.
    if check("the robot's gripper is around the mug handle and the robot's gripper is open"):
        robot.move_gripper("above the target location", close_gripper=True)
    # Slide the mug to the target location by pushing it with the gripper.
    if check("the robot's gripper is near the target location and the gripper is closed around the mug handle"):
        robot.move_gripper("horizontally aligned with the target location")