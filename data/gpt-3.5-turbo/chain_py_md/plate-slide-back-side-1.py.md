# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):

# Steps:
#  1. Open the gripper
#  2. Move the robot's gripper above the plate
#  3. Drop the gripper around the plate
#  4. Close the gripper and pick up the plate
#  5. Move the gripper to the target location
#  6. Slide the plate back into the target location
#  7. Open the gripper to release the plate

# Make sure the gripper is open before we start
if check("the robot's gripper is not open"):
    robot.release("gripper")
# Move the robot's gripper above the plate
if check("the robot's gripper is not above the plate"):
    robot.place("gripper above plate")
# Drop the gripper around the plate
if check("the gripper is not around plate"):
    robot.drop("gripper around plate")
# Close the gripper and pick up the plate
if check("the robot's gripper is not closed around plate"):
    robot.close("gripper around plate")
# Move the gripper to the target location
if check("the robot's gripper is not near target location"):
    robot.reach("to target location")
# Slide the plate back into the target location
if check("the plate is not in target location"):
    robot.slide("plate back into target location")
# Open the gripper to release the plate
if check("the robot's gripper is not open"):
    robot.release("gripper")