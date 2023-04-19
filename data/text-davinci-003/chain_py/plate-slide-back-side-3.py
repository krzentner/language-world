
    # Steps:
    #  1. Put gripper below plate
    #  2. Push the plate backwards
    #  3. Slide the plate to the target location
    # First, try to put the gripper at generally the same level as the plate.
    if check("the robot's gripper is not near plate"):
        robot.put("gripper below plate")
    # We want to move the plate back away from the edge of the table before
    # sliding it sideways.
    if check("the robot's gripper is near plate and the plate is at edge of table"):
        robot.push("plate back")
    # Once the plate is away from the edge, we can slide it to the target
    # location.
    if check("the robot's gripper is near plate and plate is away from edge of table"):
        robot.slide("plate to target")