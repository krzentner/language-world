
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop down the gripper around the handle
    #  3. Push the handle down
    # To press the handle, first the gripper needs to be above it, because the
    # robot cannot move the gripper above a handle. 
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # If the gripper is above the handle, but not around it, we can move it 
    # around the handle and then push.
    if check("the robot's gripper is above the handle and the robot's gripper is not around the handle"):
        robot.drop("gripper around handle")
    # Now that the gripper is around the handle, we can push it down.
    if check("the robot's gripper is around the handle"):
        robot.push("handle down")