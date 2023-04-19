

Steps:
1. Put gripper left of the plate
2. Grab the plate with the gripper 
3. Align the plate back with the target location 
4. Slide the plate back towards the target 

```
# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Grab the plate with the gripper
    #  3. Align the plate back with the target location
    #  4. Slide the plate back towards the target
    # Put the gripper left of the plate.
    if check("the robot's gripper is not left of the plate"):
        robot.put("gripper left of plate")
    # If the plate isn't still left of the gripper, grab it.
    if check("the plate is not left of the robot's gripper and the robot's gripper is open"):
        robot.grab("plate")
    # Now that the gripper is around the plate, line the back of the plate up
    # with the target location.
    if check("the robot's gripper is forward aligned with the plate"):
        robot.align("plate back with target location")
    # Once the back of the plate is aligned, slide the plate back towards the
    # target.
    if check("plate is back aligned with the target location"):
        robot.slide("plate back towards target")