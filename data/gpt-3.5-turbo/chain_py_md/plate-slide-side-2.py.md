```
# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Line up the plate with the target location
    #  4. Slide the plate sideways to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate is not in the gripper, grab it.
    if check("the robot's gripper is not around plate"):
        robot.grab("plate")
    # If the gripper doesn't roughly align with the target location, align it.
    if check("the plate is not roughly aligned with the target location"):
        robot.align("plate to target location")
    # If the plate is aligned with the target location on the side, slide it sideways
    # to the target location.
    if check("plate is horizontally aligned with target location"):
        robot.slide("plate sideways to target location")
```