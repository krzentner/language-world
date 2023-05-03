
    # Steps:
    #  1. Put gripper near handle
    #  2. Push down on handle
    # First, put the gripper near the handle to get a better grip.
    if check("the robot's gripper is not near the handle"):
        robot.grab("handle")
    # If the gripper is locked around the handle, we can push down.
    if check("the robot's gripper is locked around the handle"):
        robot.push("down on handle")