# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate backwards
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.place("gripper above plate")
    # If the gripper is not around the plate, move the gripper around the plate.
    if check("the robot's gripper is not around plate"):
        robot.put("gripper around plate")
    # If the gripper is around the plate and the plate is not close to the
    # target location, move the plate backwards towards the target location.
    if check("the robot's gripper is around plate and the plate is not close to the target location"):
        robot.move("plate backwards")
    # If the plate is close to target location, slide the plate sideways into
    # the target location.
    if check("the plate is close to the target location"):
        robot.slide("plate sideways into the target location")