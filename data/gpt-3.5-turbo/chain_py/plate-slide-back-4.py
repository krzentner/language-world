# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate back into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate is not gripped by the gripper, move the gripper around the
    # plate to grab it.
    if check("the plate is not gripped by the gripper"):
        robot.grab("plate")
    # If the gripper is gripped the plate, slide it back into the target location.
    if check("the plate is gripped by the gripper and the plate is not in target location"):
        robot.slide("plate back into target location")