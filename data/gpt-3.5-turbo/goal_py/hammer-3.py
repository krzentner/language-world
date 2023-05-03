# Steps:
    #  1. Align gripper with hammer head
    #  2. Close gripper around hammer handle
    #  3. Align gripper with nail
    #  4. Swing hammer down onto nail
    # First, align the gripper with the hammer head.
    if check("the robot's gripper is not near the hammer head"):
        robot.move_gripper("near the hammer head")
    # Once the gripper is near the hammer head, grab the hammer handle by
    # closing the gripper.
    if check("the robot's gripper is near the hammer head and the robot's gripper is open"):
        robot.move_gripper("around the hammer handle", close_gripper=True)
    # After grabbing the hammer handle, align the gripper with the nail.
    if check("the hammer handle is in the robot's gripper and the robot's gripper is not aligned with the nail"):
        robot.move_gripper("above the nail")
    # Finally, swing the hammer down onto the nail to hit it.
    if check("the robot's gripper is vertically aligned with the nail"):
        robot.move_gripper("below the nail")