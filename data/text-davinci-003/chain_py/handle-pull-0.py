
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up handle
    # Get the gripper above the door handle before we can grab it.
    if check("the robot's gripper is not above handle and the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    # If the gripper is above the handle, but not aligned with it or above it,
    # we should move the gripper around the handle.
    if check("the robot's gripper is above handle and the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, we should close the gripper to grab it
    # and then pull up.
    if check("the robot's gripper is around handle and the robot's gripper is open"):
        robot.close("gripper around handle")
        robot.pull("handle up")