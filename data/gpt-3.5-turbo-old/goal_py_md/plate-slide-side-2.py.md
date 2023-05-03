# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):

# Steps:
#  1. Put gripper above the plate
#  2. Grab the plate with the gripper
#  3. Line the plate up with the target location
#  4. Slide the plate sideways into the target location

# First, put the gripper above the plate.
if check("the robot's gripper is not vertically aligned with the plate"):
    robot.move_gripper("vertically aligned with the plate")
    
# If the plate becomes left of the gripper, go back to putting the gripper
# above the plate.
# Because the plate is a flat object, check if the gripper is lined up with it
# from around it instead of the front.
if check("the plate is left of the robot's gripper and the plate is not vertically aligned with the robot's gripper"):
    robot.move_gripper("vertically aligned with the plate")
    
# If the gripper isn't around the plate, put it around the plate.
if check("the robot's gripper is not around plate and the robot's gripper is open"):
    robot.move_gripper("near the plate", close_gripper=True)
    
# If the gripper is near the plate and closed, maybe we can grab it by 
# closing the gripper.
if check("the robot's gripper is around plate and the robot's gripper is closed and the robot's gripper is not horizontally aligned with plate"):
    robot.move_gripper("horizontally aligned with the plate")

# Once the plate is aligned with the target location, we can slide it.
if check("the robot's gripper is horizontally aligned with plate and the plate is horizontally aligned with target location"):
    robot.move_gripper("horizontally aligned with the target location")