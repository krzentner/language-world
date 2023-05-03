

The goal is to move the plate sideways into the target location. 

Steps:
1. Put gripper above the plate
2. Grab the plate with the gripper
3. Line the plate up with the target
4. Slide the plate sideways into the target 

if check("the robot's gripper is not above the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is not around plate and the robot's gripper is open"):
    robot.grab("plate")
if check("robot's gripper is horizontally aligned with the target, but the robot's gripper is not forward aligned with the target"):
    robot.align("plate to target")
if check("the robot's gripper is forward aligned with the target"):
    robot.slide("plate into target")