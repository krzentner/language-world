
    # Steps:
    #  1. Put gripper forward of door handle
    #  2. Push the door closed
    # If the robot's gripper is not near the door handle, we should move it
    # near the door handle.
    # We don't need to move the gripper carefully, since the robot is just going
    # to push the door closed.
    if check("the robot's gripper is not near the door handle"):
        robot.put("gripper forward of door handle")
    # If the robot's gripper is near the door handle, just start pushing the
    # door closed.
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")