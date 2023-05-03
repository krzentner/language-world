# Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper isn't around the handle and open, put it around the handle.
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is around the handle and closed, push down on the handle.
    if check("the robot's gripper is around the handle and the robot's gripper is not pushing down on it"):
        robot.move_gripper("pushing down on the handle")