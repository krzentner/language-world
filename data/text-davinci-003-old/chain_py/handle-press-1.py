
    # Steps:
    #  1. Put gripper near the handle
    #  2. Push down on the handle
    # First, move the robot's gripper near the handle, so that we can start to
    # press it down.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to the handle")
    # Now that the gripper is near the handle, push it down.
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle")