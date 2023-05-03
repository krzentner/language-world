```
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate back to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Once the gripper is lined up with the plate, grab the plate by closing the gripper.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # Once the gripper is around the plate, slide the plate back sideways to the target location.
    if check("the robot's gripper is around the plate and the plate is not at the target location"):
        robot.move_gripper("horizontally aligned with the target location")
```
