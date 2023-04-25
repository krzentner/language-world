

Steps:
1. Put gripper above plate
2. Grab plate with gripper
3. Line plate up with target location
4. Slide plate sideways into target location

If the robot's gripper is not vertically aligned with the plate, we should move the gripper near the plate to start.

if check("the robot's gripper is not vertically aligned with the plate"):
    robot.put("gripper above plate")

If the robot's gripper is near the plate we can probably slide the plate sideways now by moving the gripper.

if check("the robot's gripper is near the plate"):
    robot.grab("plate")

As long the gripper is still mostly around the plate and the plate isn't lined up with the target location, line up the plate with the target location.

if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with target location"):
    robot.align("plate to target location")

If the plate is lined up with the target location to the side, insert it.

if check("plate is horizontally aligned with target location"):
    robot.slide("plate into target location")