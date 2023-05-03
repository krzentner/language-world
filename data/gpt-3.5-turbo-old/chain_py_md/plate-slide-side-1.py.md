# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Put the plate next to the target location
    #  4. Slide the plate into the target location

    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    
    # If the gripper is almost around the plate, grab it.
    if check("the robot's gripper is forward aligned with the plate and the robot's gripper is open"):
        robot.grab("plate")
    
    # Once the gripper has the plate, position the plate next to the target location.
    if check("the gripper is holding the plate and the plate is not positioned next to the target location"):
        robot.move("plate next to target location")
    
    # Slide the plate into the target location.
    if check("the plate is positioned next to the target location"):
        robot.slide("the plate into the target location")