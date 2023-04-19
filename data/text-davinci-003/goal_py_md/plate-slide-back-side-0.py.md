

Steps:
  1. Put gripper in front of the plate
  2. Line up the plate with the target location
  3. Slide the plate backwards into the target location

If the robot's gripper is not in front of the plate, move it to the plate.
```

# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper in front of the plate
    #  2. Line up the plate with the target location
    #  3. Slide the plate backwards into the target location
    # If the robot's gripper is not in front of the plate, move it to the plate.
    if check("the robot's gripper is not in front of the plate"):
        robot.move_gripper("in front of the plate")
    # Once the gripper is in front of the plate, we need to line it up with the
    # target location.
    if check("the robot's gripper is in front of the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the plate is lined up with the target location, we can slide it back
    # into the target location.
    if check("the plate is horizontally aligned with the target location"):
        robot.move_gripper("near the plate")