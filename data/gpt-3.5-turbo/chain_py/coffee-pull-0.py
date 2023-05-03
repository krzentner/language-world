# Steps:
    #  1. Put gripper above handle
    #  2. Open gripper and drop around handle
    #  3. Close gripper around handle
    #  4. Pull mug to target location
    # First, put the gripper roughly above the handle, so that we don't bump the
    # mug while trying to grab it.
    if check("the robot's gripper is not above the coffee mug handle"):
        robot.move("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is near the handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    # We closed the gripper, and the handle is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the mug to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around handle and the mug is being pulled towards target"):
        robot.pull("coffee mug to target location")