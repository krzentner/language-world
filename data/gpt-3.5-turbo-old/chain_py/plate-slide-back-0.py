# Steps:
    #  1. Put the gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate backwards into the target location
    # First, the robot should put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the gripper is not around the plate, the robot should grab the plate with
    # the gripper.
    if check("the robot's gripper is not around the plate"):
        robot.grab("plate with the gripper")
    # If the gripper is holding the plate, the robot should slide it back into the
    # target location.
    if check("the plate is being held by the gripper"):
        robot.slide("the plate into the target location")