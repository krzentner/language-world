# Steps:
    #  1. Put gripper roughly around the handle
    #  2. Push down on the handle from the side
    # We need to put the gripper around the handle before we can push it down.
    if check("the robot's gripper is not around the handle"):
        robot.grab("handle")
    # If the gripper is around the handle, we can push down on the handle from the
    # side.
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle from the side")