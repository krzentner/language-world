

Steps:
1. Put gripper forward of the plate
2. Grab the plate with the gripper
3. Move the plate until it's aligned with the target location
4. Slide the plate sideways into the target location

If the robot's gripper is not forward of the plate, move the gripper near the plate to start sliding.

```
# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper forward of the plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate until it's aligned with the target location
    #  4. Slide the plate sideways into the target location
    # If the robot's gripper is not forward of the plate, move the gripper near the plate to start sliding.
    if check("the robot's gripper is not forward of the plate"):
        robot.move_gripper("forward of the plate", close_gripper=True)
    # If the plate is now left of the robot's gripper, move the plate until it's aligned with the target location.
    if check("the plate is not horizontally aligned with the target location"):
        robot.move_gripper("above the plate")
    # If the plate is horizontally aligned with the target location, slide it sideways into the target location.
    if check("the plate is horizontally aligned with the target location"):
        robot.move_gripper("left of the target location")