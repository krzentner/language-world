```
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate back sideways into the target location

    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is above the plate, move it down to grab the plate.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # Once the gripper has the plate, line it up with the target location.
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # Finally, slide the plate back into the target location.
    if check("the robot's gripper is around the plate and the plate is horizontally aligned with the target location"):
        robot.move_gripper("backwards of the target location") 
```