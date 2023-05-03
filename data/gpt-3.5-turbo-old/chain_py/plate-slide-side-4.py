# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Line up the plate with the target location, but keep the plate raised above the surface
    #  4. Slide the plate sideways into the target location while lowering it to the surface
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Once the gripper is above the plate, grab it.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.grab("plate")
    # While holding the plate, line it up with the target location but above the surface.
    if check("the plate is grabbed by the robot's gripper and the plate is not lined up with the target location"):
        robot.align("plate to target location")
        robot.raise("plate above surface")
    # Once the plate is lined up and raised above the surface, slide it into the target location while lowering it.
    if check("the plate is lined up with the target location and is above the surface"):
        robot.slide("plate into the target location while lowering it to the surface")