

Steps:
     1. Put gripper above plate
     2. Grab plate with gripper
     3. Line plate up with the target location
     4. Slide plate sideways into target location

# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above plate")
    #  2. Grab plate with gripper
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.move_gripper("near plate", close_gripper=True)
    #  3. Line plate up with the target location
    if check("the robot's gripper is around plate and the plate is not sideways aligned with the target location"):
        robot.move_gripper("sideways aligned with target location")
    #  4. Slide plate sideways into target location
    if check("the robot's gripper is around plate and the plate is sideways aligned with the target location"):
        robot.move_gripper("near the target location")