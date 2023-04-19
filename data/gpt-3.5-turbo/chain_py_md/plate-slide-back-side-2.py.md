# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate back and sideways to target location
    # First, put the gripper above the plate to avoid bumping into the plate while moving it.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Once the gripper is above the plate, grab it.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.grab("the plate")
    # If the gripper is now holding the plate, move the plate back and sideways to the target location.
    if check("the robot's gripper is around the plate"):
        robot.slide("the plate back and sideways to the target location")