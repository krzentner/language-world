
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Pull mug to goal
    # First, put the gripper above the mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    # If the gripper is near the mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # We closed the gripper, and the mug is still near the gripper, so maybe we
    # grabbed it.
    # Try to pull the mug to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.pull("mug to goal")