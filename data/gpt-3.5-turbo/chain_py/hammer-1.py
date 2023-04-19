# Steps:
#  1. Grab the hammer
#  2. Line up the hammer with the nail
#  3. Swing the hammer down to hit the nail
# First, put the gripper around the hammer.
if check("the robot's gripper is not around the hammer"):
    robot.grab("hammer")
# Line up the hammer with the nail.
if check("the robot's gripper is around the hammer and the hammer is not aligned with the nail"):
    robot.align("hammer with nail")
# Swing the hammer down to hit the nail.
if check("the robot's gripper is around the hammer and the hammer is aligned with the nail"):
    robot.swing("hammer to hit the nail")