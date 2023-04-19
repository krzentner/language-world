

Steps:
1. Put gripper above the plate
2. Grab the plate with the gripper
3. Line up the plate with the target location
4. Slide the plate sideways into the target

if check("the robot's gripper is not vertically aligned with the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is not around the plate"):
    robot.grab("plate")
if check("the plate is not horizontally aligned with the target location"):
    robot.align("plate to target")
if check("the plate is horizontally aligned with the target location"):
    robot.slide("plate to target")