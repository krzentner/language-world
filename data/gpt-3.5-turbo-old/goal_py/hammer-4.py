# Steps:
#  1. Pick up the hammer
#  2. Position the hammer above the nail
#  3. Rotate the wrist to hit the nail
#  4. Lift the hammer back up
# First, put the gripper around the hammer handle and lift it off the table.
if check("the robot's gripper is not around the hammer handle"):
    robot.move_gripper("around the hammer handle", close_gripper=True)
# Once the gripper is around the hammer handle, lift it towards the nail.
if check("the robot's gripper is not above the nail"):
    robot.move_gripper("above the nail")
# Rotate the gripper to hit the nail.
if check("the robot's gripper is above the nail and the wrist is not rotated correctly"):
    robot.rotate_wrist("correct rotation")
# Bring the hammer back up.
if check("the robot's gripper is above the nail and the wrist is rotated correctly"):
    robot.move_gripper("above the nail", close_gripper=False)