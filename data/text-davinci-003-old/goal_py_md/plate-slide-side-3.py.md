

The steps are:
1. Put gripper above the plate
2. Grab the plate with the gripper
3. Line the plate up with the the target location
4. Slide the plate sideways into the target location

Solution:

# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper roughly above the plate, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the plate isn't below the gripper as seen from above, move the gripper
    # above the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate and open, we can grab it by closing the
    # gripper.
    if check("the robot's gripper is above plate and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
    # If the plate is not lined up with the target location, line it up
    # horizontally to the side.
    if check("the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # Once the plate is lined up with the target location, slide it into the
    # target location.
    if check("the plate is horizontally aligned with the target location"):
        robot.move_gripper("above the plate")