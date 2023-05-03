# Steps:
    #  1. Put gripper over the hammer handle
    #  2. Grab the hammer handle
    #  3. Line up the hammer head with the nail
    #  4. Swing the hammer down onto the nail
    # First, put the gripper roughly over the hammer handle.
    if check("the robot's gripper is not above the hammer handle"):
        robot.place("gripper above hammer handle")
    # If the gripper isn't around the hammer handle, put it around the handle.
    if check("the robot's gripper is not around hammer handle and the robot's gripper is open"):
        robot.drop("gripper around hammer handle")
    # If the gripper is near the handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near hammer handle and gripper is open"):
        robot.close("gripper around hammer handle")
    # We closed the gripper, and the hammer should be lined up with the nail, so
    # swing the hammer down onto the nail.
    if check("the robot's gripper is around hammer handle"):
        robot.swing("hammer onto nail")