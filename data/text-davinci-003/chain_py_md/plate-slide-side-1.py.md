

## Solution

```
# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper vertically above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the gripper isn't around the plate, move it around the plate.
    if check("the robot's gripper is not around plate):
        robot.drop("gripper around plate")
    # If the plate isn't lined up with the target location, rotate it so that
    # it is.
    if check("the plate is not aligned with the target location"):
        robot.align("plate to target")
    # If the plate is lined up with the target location and the gripper is around
    # the plate, slide the plate into the target location.
    if check("the plate is aligned with the target location and the robot's gripper is around the plate"):
        robot.slide("plate to target")
```