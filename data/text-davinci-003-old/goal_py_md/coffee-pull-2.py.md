

Steps:
1. Put gripper above mug handle
2. Drop gripper around mug handle
3. Pull mug to the target location

if check("the robot's gripper is not vertically aligned with mug handle"):
    robot.move_gripper("vertically aligned with the mug handle")
if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
    robot.move_gripper("around the mug handle")
if check("the robot's gripper is around mug handle and the robot's gripper is not near target location"):
    robot.move_gripper("near the target location")