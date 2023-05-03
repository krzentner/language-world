# hammer: hit the nail with the hammer
# def hammer(robot):
# Steps:
# 1. Put gripper above the hammer
# 2. Grab the handle of the hammer with the gripper
# 3. Put gripper above the nail
# 4. Bring hammer down to hit the nail
# 5. Release the hammer

# First, put the gripper above the hammer.
if check("the robot's gripper is not vertically aligned with the hammer"):
    robot.move_gripper("vertically aligned with the hammer")
# If the gripper is not around the handle of the hammer, put it around the handle.
if check("the robot's gripper is not around the handle of the hammer and the robot's gripper is open"):
    robot.move_gripper("near the handle of the hammer", close_gripper=True)
# Once the gripper is around the handle of the hammer, put it above the nail.
if check("the robot's gripper is around the handle of the hammer and the robot's gripper is not vertically aligned with the nail"):
    robot.move_gripper("vertically aligned with the nail")
# Move the gripper and hammer to hit the nail.
if check("the robot's gripper is above the nail and the hammer has not hit the nail"):
    robot.move_gripper("almost touching the nail")
# After hitting the nail, release the hammer.
if check("the hammer has hit the nail"):
    robot.move_gripper("near the hammer", open_gripper=True)