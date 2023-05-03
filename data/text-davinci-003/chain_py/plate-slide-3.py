
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper onto plate
    #  3. Slide plate to goal
    # First, put the gripper above the plate. We want to be careful not to bump
    # the plate while trying to grab it.
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.put("gripper above plate")
    # Now that the gripper is near the plate, we can lower the gripper onto the
    # plate to start sliding it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is open"):
        robot.drop("gripper onto plate")
    # Now that the gripper is on the plate, we can slide the plate to the
    # target location.
    if check("the robot's gripper is above the plate and the robot's gripper is closed"):
        robot.slide("plate to goal")