# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with gripper
    #  3. Slide the plate back to the target location
    
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    
    # Once the gripper is above the plate, grab it.
    if check("the robot's gripper is above the plate"):
        robot.grab("plate")
    
    # Now that the plate is secured, slide it back sideways to the target location.
    if check("the plate is in the gripper"):
        robot.slide("plate back to the goal")