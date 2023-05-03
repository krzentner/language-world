

Then fill in the remaining code:

```
# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Trap the plate between the gripper and the surface
    #  3. Slide the plate to the target location
    # First, move the gripper above the plate.
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper
    # down to the plate to trap it between the gripper and the surface.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is near the plate, the plate should be trapped and we can
    # move it to the target location.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.move_gripper("above the target location")
```