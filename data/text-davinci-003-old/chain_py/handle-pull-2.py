
    # Steps:
    #  1. Grab the handle from above
    #  2. Pull the handle up
    # To pull the handle, we first need to grab it from above.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above the handle")
    # When the gripper is above the handle, close the gripper to grab it.
    if check("the robot's gripper is vertically aligned with the handle and the gripper is open"):
        robot.close("gripper around the handle")
    # Now that the gripper is closed around the handle, we can pull the handle.
    if check("the robot's gripper is around the handle and the gripper is closed"):
        robot.pull("handle up")