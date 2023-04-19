# Steps:
    #  1. Put the gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not above the mug"):
        robot.place("gripper above mug")
    # If the gripper isn't around the mug, put it around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    # If the gripper is near the mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # We closed the gripper, and the mug is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the mug to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.place("mug at goal")