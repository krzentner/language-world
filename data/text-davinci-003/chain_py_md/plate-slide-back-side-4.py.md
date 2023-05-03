

The plate must be slid into a hole or other target location from the side. The robot's gripper should grab the plate, since it is a small object, then adjust its angle and slide the plate back until it is fully in the target location. 

Steps:
1. Put gripper above the plate
2. Grab the plate with the gripper
3. Line up the back side of the plate with the target location
4. Slide the plate back sideways into the target location

```
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line up the back side of the plate with the target location
    #  4. Slide the plate back sideways into the target location
    # First, we need to put the gripper above the plate
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # Once the gripper is lined up above the plate, we can grab the plate with
    # the robot's gripper.
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is open"):
        robot.grab("plate with gripper")
    # Now that the plate is grabbed with the robot's gripper, we should line up
    # the back of the plate with the target location.
    if check("the back side of the plate is not aligned with the target location and the robot's gripper is closed around the plate"):
        robot.put("back side of plate by target location")
    # If the back side of the plate is aligned with the target location, we can
    # slide it back into the target location.
    if check("the back side of the plate is aligned with the target location"):
        robot.slide("plate back into target location")
```