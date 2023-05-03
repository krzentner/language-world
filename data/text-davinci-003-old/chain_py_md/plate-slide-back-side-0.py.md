

Steps: 
1. Put gripper above plate
2. Grab the plate with the gripper
3. Line up the plate with the target location
4. Slide the plate backwards and to the side

```
# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps: 
    #  1. Put gripper above plate 
    # We don't need to be super precise here, just roughly above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the plate isn't below the gripper as seen from above, move the gripper 
    # above the plate.
    if check("the robot's gripper is not under the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above the plate")
    # If the gripper is aligned with the plate but not near it, move the gripper 
    # down to the plate to grab it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.grab("the plate")
    # If the gripper is above the plate and the plate is below the gripper (we 
    # have control of the plate) we need to line up the plate with the target 
    # location. 
    if check("the robot's gripper is above the plate and the plate is below the robot's gripper"):
        robot.align("the plate with the target location")
    # Once the plate is aligned, we can slide it backwards and to the side towards
    # the target location. 
    if check("the plate is aligned with the target location"):
        robot.slide("plate backwards and to the side")
```