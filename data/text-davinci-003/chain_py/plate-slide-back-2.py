
    # Steps:
    #  1. Put gripper near plate
    #  2. Push plate back into target location
    # First, move the gripper near the plate so it can start pushing the plate.
    if check("the robot's gripper is not near plate"):
        robot.put("gripper near plate")
    # Once the gripper is near the plate, slide it back and push against the
    # table.
    if check("the robot's gripper is near plate and the plate is not back in the target location"):
        robot.push("plate back")