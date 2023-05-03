# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate
    #  3. Move plate to the target location horizontally
    #  4. Align the plate with the target location vertically
    #  5. Slide the plate into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper is not around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.grab("the plate")
    # Move the plate horizontally to the target location,
    # if it is not aligned horizontally with the target location.
    if check("the plate is not horizontally aligned with the target location"):
        robot.move("plate to the target location horizontally")
    # Align the plate with the target location vertically,
    # if it is not aligned vertically with the target location.
    if check("the plate is not vertically aligned with the target location"):
        robot.align("plate to the target location vertically")
    # Slide the plate into the target location.
    if check("the plate is aligned with the target location"):
        robot.slide("the plate into the target location")