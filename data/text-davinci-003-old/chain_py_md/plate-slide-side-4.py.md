

Here's the program to perform the `plate-slide-side` task:

```
# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a flat object, check if the gripper is lined up with
    # it from the top instead of around it.
    if check("plate is not left of the robot's gripper and plate is not vertically aligned with the robot's gripper"):
        robot.grab("plate")
    # As long the gripper is still mostly around the plate and the plate isn't lined
    # up with the target, line up the plate with the target.
    if check("the robot's gripper is vertically aligned with the plate and the plate is not horizontally aligned with target"):
        robot.align("plate to target")
    # If the plate is lined up with the target to the side, slide it into the target location.
    if check("plate is horizontally aligned with target"):
        robot.slide("plate into target")
```