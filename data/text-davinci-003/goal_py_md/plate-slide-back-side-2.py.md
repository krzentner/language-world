

The goal of this task is to move a plate into a target location.

Steps:
1. Put gripper above the plate
2. Push gripper into the back of the plate
3. Slide the plate into the target location

# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Next, push the gripper into the back of the plate.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
        robot.move_gripper("left of the plate", close_gripper=True)
    # Finally, slide the plate into the target location.
    if check("the robot's gripper is near the plate and the plate is not left of the robot's gripper"):
        robot.move_gripper("near the target location")