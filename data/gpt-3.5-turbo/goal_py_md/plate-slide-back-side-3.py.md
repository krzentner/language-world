```
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move the plate back towards the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Once the gripper is lined up above the plate, we can grab the plate by moving
    # the gripper down around it.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # After grabbing the plate, move the gripper back to the target location.
    if check("the robot's gripper is around the plate and the robot's gripper is not horizontally aligned with the target location"):
        robot.move_gripper("almost horizontally aligned with the target location")
    # Slide the plate sideways into the target location.
    if check("the robot's gripper is horizontally aligned with the target location and the plate is between the robot gripper and the target location"):
        robot.move_gripper("into the target location along the side of the plate")
```