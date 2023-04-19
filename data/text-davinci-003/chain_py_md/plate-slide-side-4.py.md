

Steps:
1. Put gripper above the plate
2. Grab the plate with the gripper
3. Line the plate up with the target
4. Slide the plate sideways into the target

If the robot's gripper is not vertically aligned with the plate, we should move the gripper above the plate.
if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")

If the plate becomes left of the gripper, go back to putting the gripper above the plate.
if check("the plate is not left of the robot's gripper and the plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")

As long the gripper is still mostly around the plate and the plate isn't lined up with the target, line up the plate with the target.
if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with target"):
        robot.align("plate to target")

If the plate is lined up with the target to the side, insert it.
if check("plate is horizontally aligned with target"):
        robot.insert("plate into target")