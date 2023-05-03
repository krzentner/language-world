# Steps:
#  1. Line up the gripper above the lid handle
#  2. Open the gripper and place it around the lid
#  3. Close the gripper around the lid
#  4. Move the lid to the box 
# First, line up the gripper above the lid handle.
if check("the robot's gripper is not above the lid handle and the robot's gripper is not vertically aligned with the lid handle"):
    robot.move_gripper("vertically aligned with the lid handle")
# If the gripper is above the lid handle, open it and place it around the lid.
if check("the robot's gripper is above the lid handle and the robot's gripper is not around the lid"):
    robot.move_gripper("near the lid", close_gripper=False)
# Once the gripper is around the lid, close the gripper to hold it.
if check("the robot's gripper is around the lid and the gripper is open"):
    robot.move_gripper("near the box")
# Finally, move the lid to the box and release it.
if check("the robot's gripper is near the box and the gripper is closed"):
    robot.move_gripper("above the box", close_gripper=False)