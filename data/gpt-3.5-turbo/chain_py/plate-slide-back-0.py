# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate back towards the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the gripper is not open and not around the plate, release the plate.
    if check("the robot's gripper is not open and the robot's gripper is not around the plate"):
        robot.release("plate")
    # Grab the plate with the gripper if it is open and above it.
    if check("the robot's gripper is open and the robot's gripper is above the plate"):
        robot.grab("plate")
    # If the gripper is holding the plate, slide the plate towards the target location.
    if check("the robot's gripper is holding the plate and the plate is not at the target location"):
        robot.slide("plate back to target location")