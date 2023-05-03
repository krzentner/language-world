# Steps:
    #  1. Put hand above the hammer
    #  2. Grab the handle of the hammer
    #  3. Position the hammer over the nail
    #  4. Swing the hammer down onto the nail
    # First, put the gripper roughly above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.move_gripper("above the hammer")
    # If the gripper isn't around the hammer, put it around the handle.
    if check("the robot's gripper is not around the hammer and the robot's gripper is open"):
        robot.move_gripper("near the hammer handle", close_gripper=True)
    # If the gripper is around the hammer, position it over the nail.
    if check("the robot's gripper is around the hammer handle and the robot's gripper is not vertically aligned with the nail"):
        robot.move_gripper("vertically aligned with the nail")
    # If the gripper is positioned over the nail, swing the hammer down onto it.
    if check("the robot's gripper is vertically aligned with the nail"):
        robot.move_gripper("horizontally aligned with the nail")