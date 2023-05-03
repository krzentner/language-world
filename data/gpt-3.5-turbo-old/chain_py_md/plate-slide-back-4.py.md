# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    # Steps:
    # 1. Put gripper above plate
    # 2. Grab the plate with the gripper
    # 3. Slide the plate back to target location 
    # First, put the gripper roughly above the plate.
    if check("the robot's gripper is not roughly above the plate"):
        robot.place("gripper above plate")
    # Now, grab the plate with the gripper.
    if check("the robot's gripper is not holding the plate and the gripper is above the plate"):
        robot.grab("plate")
    # Once the plate is held by the gripper, slide it back towards the target location.
    if check("the plate is held by the gripper and the gripper is near the target location"):
        robot.slide("the plate back to target location")