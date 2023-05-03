
    # Steps:
    #  1. Put gripper above plate    
    #  2. Grab the plate with the gripper
    #  3. Slide the plate to the target location
    # First, put the gripper above the plate
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above the plate")
    # Once the gripper is above the plate, we should be able to grab it.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.grab("plate")
    # If the gripper is in contact with the plate, slide the plate to the
    # target location.
    if check("the robot's gripper is in contact with the plate"):
        robot.slide("plate to target location")