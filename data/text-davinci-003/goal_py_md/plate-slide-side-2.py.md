

Steps:
  1. Put gripper right of the plate 
  2. Grab the plate with the gripper
  3. Line the plate up with the target location 
  4. Slide the plate sideways into the target location 

```
# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper right of the plate 
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location 
    #  4. Slide the plate sideways into the target location
    # First, put the gripper to the right of the plate.
    if check("the robot's gripper is not right of the plate"):
        robot.move_gripper("right of the plate")
    # If the gripper is now left of the plate, move it back above the plate.
    if check("the robot's gripper is left of the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Now that the gripper is lining up with the plate, try to grab it by
    # closing the gripper.
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not around plate"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # If the plate is aligned with the target location, we can attempt to
    # slide it sideways.
    if check("the plate is forward aligned with target location"):
        robot.move_gripper("horizontally aligned with target location")
    # If the plate is not yet aligned with the target location, rotate it until
    # it is.
    if check("the plate is not horizontally aligned with target location"):
        robot.move_gripper("forward aligned with target location")