
    # Steps:
    #  1. Put gripper near handle
    #  2. Close the gripper around handle
    #  3. Pull upward with the handle
    # If the gripper is not near the handle, move it to the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper near handle")
    # If the gripper is near the handle, close the gripper around it.
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    # Now that the gripper is closed around the handle, pull it upward.
    if check("the robot's gripper is closed around the handle"):
        robot.pull("handle up")