```
# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not lined up with the center of the plate"):
        robot.move_gripper("centered above the plate")
    # If the gripper is not around the plate, move the gripper around the plate
    # and close it to grab the plate.
    if check("the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # If the gripper is around the plate, line it up with the target location.
    if check("the robot's gripper is around the plate and not near the target location"):
        robot.move_gripper("near the target location", close_gripper=True)
    # If the gripper is near the target location, slide the plate sideways to
    # the target location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("horizontally aligned with the target location")
```