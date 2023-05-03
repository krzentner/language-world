
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Close gripper around mug handle
    #  3. Pull the mug towards goal
    # First, put the gripper above coffee mug handle, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above coffee mug handle"):
        robot.put("gripper above coffee mug handle")
    # If the gripper isn't around the coffee mug handle, put it around the
    # coffee mug handle.
    if check("the robot's gripper is not around the coffee mug handle and the robot's gripper is open"):
        robot.drop("gripper around coffee mug handle")
    # If the gripper is near the coffee mug handle and open, maybe we can grab it
    # by closing the gripper.
    if check("the robot's gripper is near coffee mug handle and the robot's gripper is open"):
        robot.close("gripper around coffee mug handle")
    # We closed the gripper, and the coffee mug is still near the gripper, so
    # maybe we grabbed it.
    # Try to move the coffee mug to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above coffee mug handle and the robot's gripper is closed"):
        robot.pull("mug to goal")