# Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with gripper
    #  3. Move gripper towards the target location
    #  4. Release plate at the target location
    # First, put the gripper above the plate to avoid hitting it.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # Once the gripper is above the plate, we can grab it.
    if check("the robot's gripper is above plate and the robot's gripper is open"):
        robot.grab("plate")
    # Once the gripper is around the plate, move it towards the target location
    # by sliding it sideways.
    if check("the robot's gripper is around plate and the plate is not at goal location"):
        robot.slide("plate towards goal")
    # Once the plate has been moved to the target location, release it.
    if check("the plate is at goal location and the robot's gripper is holding plate"):
        robot.release("plate at goal location")