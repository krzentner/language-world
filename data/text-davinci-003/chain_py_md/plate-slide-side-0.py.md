  


# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around plate
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Once the gripper is above the plate, close the gripper around it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # As long the gripper is still around the plate and the plate isn't lined
    # up with the target location, line up the plate with the target location.
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with target location"):
        robot.align("plate to target location")
    # If the plate is lined up with the target location to the side, insert it.
    if check("plate is horizontally aligned with target location"):
        robot.insert("plate into target location")