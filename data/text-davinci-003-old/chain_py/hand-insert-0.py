
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Reach toward the target
    #  5. Insert the puck into the target
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.reach("to target")
    # Once the gripper is above the target, we can insert the puck.
    if check("the robot's gripper is above the target"):
        robot.insert("puck into target")