
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Close gripper around handle
    #  4. Pull the mug to goal
    # First, put the gripper roughly above the handle, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is near the handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    # We closed the gripper, and the mug handle is still near the gripper, so
    # maybe we grabbed it.
    # Try to move the mug handle to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above handle and the robot's gripper is closed"):
        robot.pull("mug to goal")