
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Push the handle down
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # If the handle is below the robot's gripper, grab it with the gripper.
    # We don't need to be careful about the direction here, since the handle is
    # small and we're just squeezing it (unlike when opening a drawer).
    if check("the handle is below the robot's gripper"):
        robot.grab("handle")
    # If the handle is between the gripper's fingers, push down on it.
    if check("the handle is between the robot's gripper's fingers"):
        robot.push("handle down")