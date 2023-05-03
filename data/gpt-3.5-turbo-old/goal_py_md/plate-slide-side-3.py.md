# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
# Steps:
#   1. Put gripper above plate
#   2. Grab the plate with the gripper
#   3. Line the plate up with the target location
#   4. Slide the plate sideways into the target location
# First, put the gripper above the plate.
if check("the robot's gripper is not vertically aligned with the plate"):
    robot.move_gripper("vertically aligned with the plate")
# If the plate becomes left of the gripper, go back to putting the gripper above the plate.
# Because the plate is a large object, check if the gripper is lined up with it
# around it instead of from the front.
if check("plate is not left of the robot's gripper and plate is not horizontally aligned with the robot's gripper"):
    robot.move_gripper("horizontally aligned with the plate", close_gripper=True)
# If the plate is aligned with the target location to the side, slide it into the target location.
if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):
    robot.move_gripper("horizontally aligned with the target location")