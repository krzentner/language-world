# Steps:
#  1. Pick up the stick
#  2. Move the stick to the thermos
#  3. Use the stick to push the thermos to the target location
# First, put the gripper around the stick.
if check("the robot's gripper is not around the stick and the robot's gripper is open"):
    robot.move_gripper("near the stick", close_gripper=True)
# Once the gripper is around the stick, move it to the thermos.
if check("the robot's gripper is around the stick and the robot's gripper is not near thermos"):
    robot.move_gripper("above the thermos")
# Once the gripper is near the thermos, use the stick to push the thermos to the
# target location.
if check("the robot's gripper is near the thermos"):
    robot.move_gripper("above the target location")