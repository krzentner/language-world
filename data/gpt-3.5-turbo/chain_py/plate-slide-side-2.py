# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate towards the target location
    #  4. Slide the plate into the target location from the side
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper is not around the plate, grab it.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # Move the plate towards the target location.
    if check("the robot's gripper is around the plate and the plate is not near the target location"):
        robot.move("plate towards target location")
    # Slide the plate from the side into the target location.
    if check("the plate is near the target location"):
        robot.slide("plate into target location from the side")