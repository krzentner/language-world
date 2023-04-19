

Steps:
  1. Put the gripper above the plate
  2. Drop the gripper around the plate
  3. Align the plate with the target location
  4. Slide the plate sideways into the target location

# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put the gripper above the plate
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    #  2. Drop the gripper around the plate
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.drop("gripper around plate") 
    #  3. Align the plate with the target location
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with the target location"):
        robot.align("plate with target location")
    #  4. Slide the plate sideways into the target location
    if check("the plate is horizontally aligned with the target location"):
        robot.slide("plate into target location")